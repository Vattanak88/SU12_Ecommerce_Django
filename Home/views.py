import os
import shutil
import time
import uuid
from http.client import responses
from itertools import product
from json import JSONDecodeError
from locale import currency
from pathlib import Path
from urllib.parse import quote_plus

from django.core import serializers
from django.http import BadHeaderError, HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
import requests
from django.templatetags.static import static
from django.views.decorators.http import require_http_methods
from pyexpat.errors import messages
from tabulate import tabulate
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import json
import traceback
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bakong_khqr import KHQR
import qrcode
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get Bakong token from environment, fallback to hardcoded (use .env in production)
bakong_token = os.getenv('BAKONG_TOKEN', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImlkIjoiYzNhYjk1OGMxYzljNDE1YSJ9LCJpYXQiOjE3NjE0NzEwOTEsImV4cCI6MTc2OTI0NzA5MX0.gVv1mcVp1o0hNrXqe5DOodFg3LIWQUfO3kL8Ems7zL4')


def check_payment_status(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    try:
        # Parse JSON safely
        data = json.loads(request.body)
        md5 = data.get('md5')

        if not md5:
            return JsonResponse({"error": "md5 is required"}, status=400)

        url = "https://api-bakong.nbc.gov.kh/v1/check_transaction_by_md5"

        res = requests.post(
            url,
            json={"md5": md5},
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {bakong_token}",
            },
            timeout=30
        )

        res.raise_for_status()

        return JsonResponse(res.json(), safe=False)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except requests.exceptions.Timeout:
        return JsonResponse({"error": "API timeout"}, status=504)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=502)
    except Exception as e:
        return JsonResponse({"error": f"Unexpected error: {str(e)}"}, status=500)

def payment(request):
    data = request.session.get('qr_code', {})

    context = {
        "md5": data.get("md5"),
        "total_payment": data.get("total_payment"),
        "currency_type": data.get("currency_type"),
        "merchant_name": data.get("merchant_name"),
        "title" : 'payment_page',
        "filename" : data.get("filename")
    }

    return render(request, "payment.html", context)

def success(request):
    context = {
        'title' : 'Payment Successful'
    }
    return render(request, "success.html", context)

@api_view(['POST'])
def qr_generate(request):
    if request.method == 'POST':
        try :
            data = request.data

            total_payment = data.get("total_payment")
            currency_type = data.get("currency_type")

            khqr = KHQR(bakong_token)

            # Get Bakong merchant details from .env
            bank_account = os.getenv('BAKONG_MERCHANT_ACCOUNT', 'meng_sonly@wing')
            merchant_name = os.getenv('BAKONG_MERCHANT_NAME', 'MENG SONLY')
            merchant_city = os.getenv('BAKONG_MERCHANT_CITY', 'Phnom Penh')
            phone_number = os.getenv('BAKONG_PHONE_NUMBER', '85510947790')
            store_label = os.getenv('BAKONG_STORE_LABEL', 'LyCoding')
            terminal_label = os.getenv('BAKONG_TERMINAL_LABEL', 'Lycod01')

            # Generate QR code data for a transaction:
            qr = khqr.create_qr(
                bank_account=bank_account,
                merchant_name=merchant_name,
                merchant_city=merchant_city,
                amount=total_payment,
                currency=currency_type,
                store_label=store_label,
                phone_number=phone_number,
                bill_number='order_' + str(uuid.uuid4())[:8],
                terminal_label=terminal_label,
                static=False
            )

            # get hash md5
            md5 = khqr.generate_md5(qr)
            img = qrcode.make(qr) 
            filename = f"{md5}.png"
            file_path = os.path.join(settings.MEDIA_ROOT, "qrcodes", filename) 
            img.save(file_path)   
            request.session['qr_code'] = {
                "md5": md5,
                "total_payment": total_payment,
                "currency_type": currency_type,
                "merchant_name": merchant_name,
                "filename": filename
            }

            # Send JSON response with the redirect URL to the payment page
            return JsonResponse({
                "redirect": "/payment"
            })

        except Exception as e:
            print("Exception in qr_generate:", str(e))
            print(traceback.format_exc())
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    else:
        return JsonResponse({
            'status': 'error',
            'message' : 'This method is not allow.',

        }, status=400)


def index(request):
    slider = Slider.objects.filter(status = 'active')
    features = Feature.objects.all()
    features_dict = [feature.as_dict() for feature in features]
    size = len(slider)

    context = {
        'title': 'Index', 
        'sliders': slider,
        'feature': features_dict,
        'size': size,
    }

    print(features_dict)

    return render(request, 'index.html',context)

def shop(request):
    context = {
        'title': 'Shop'
    }

    return render(request, 'shop.html',context)

def contact(request):
    context = {
        'title': 'Contact'
    }

    return render(request,'contact.html',context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request,'aboutus.html',context)

def checkout(request): 
    carts = Cart.objects.values('image','qty','name','price').filter(status=True)

    context = {
        'title': 'Checkout',
        'carts': carts,
    }
    return render(request,'checkout.html',context)

def cart(request):
    carts = Cart.objects.all()
    cart_count = carts.count()

    context = {
        'title': 'Cart',
        'carts': carts,
        'cart_count': cart_count,
    }

    return render(request,'cart.html',context)

def payment_page(request):

    context = {
        'title': 'payment_page',
        'name' : 'meng sonly'
    }

    return render(request,'payment.html',context)

def fetchproducts(request):
    products = Product.objects.all()
    data = [product.as_dict() for product in products]

    return JsonResponse(data, safe=False)

def productdetails(request):
    context = {'title': 'ProductDetails'}

    return render(request, 'productdetail.html', context)

def email_sender(request):
    context = {}
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        from_email = request.POST.get('from_email')
        your_message = request.POST.get('your_message')
        fullname = f"{first_name} {last_name}"

        if fullname and from_email and your_message:
            try:

                send_mail(
                    f"Message from {fullname}",  # Subject line
                    your_message,  # Message content
                    from_email,  # Sender's email
                    ['sample@gmail.com'],  # Recipient email
                    fail_silently=False
                )

                context = {
                    'result' : 'Email Sent Successfully'
                }
                print(from_email)
            except Exception as e:
                context = {
                    'result': f'Error Email Sending : {e}'
                }
    return render(request,'contact.html',context)

@api_view(['POST'])
def add_to_cart(request):
    if request.method == 'POST':
        try:
            data = request.data
            print("\n=== ADD_TO_CART DEBUG ===")
            print(f"Received data type: {type(data)}")
            print(f"Received data: {data}")
            
            # Ensure data is a list
            if isinstance(data, dict):
                data = [data]
            elif not isinstance(data, list):
                print(f"Invalid payload type: {type(data).__name__}")
                print("=== END ADD_TO_CART DEBUG ===\n")
                return JsonResponse({'error': f'Invalid payload type: {type(data).__name__}, expected array or object'}, status=400)

            print(f"Processing {len(data)} items")

            # Process each item in the cart list
            for idx, item in enumerate(data):
                if not isinstance(item, dict):
                    print(f"Item {idx} is not a dict: {type(item).__name__}")
                    print("=== END ADD_TO_CART DEBUG ===\n")
                    return JsonResponse({'error': f'Item {idx} is not a valid object'}, status=400)
                
                product_id = item.get('product_id')
                if not product_id:
                    print("product_id is required")
                    print("=== END ADD_TO_CART DEBUG ===\n")
                    return JsonResponse({'error': 'product_id is required for each item'}, status=400)

                try:
                    qty = int(item.get('qty', 1))
                except Exception:
                    qty = 1

                existing_item = Cart.objects.filter(product_id=product_id).first()

                if existing_item:
                    existing_item.qty += qty
                    existing_item.save()
                    print(f"Updated qty for product_id={product_id}, new qty={existing_item.qty}")
                else:
                    Cart.objects.create(
                        product_id=product_id,
                        name=item.get('name'),
                        image=item.get('image'),
                        qty=qty,
                        status=item.get('status', True),
                        price=item.get('price', 0),
                    )
                    print(f"Added new product_id={product_id}")

            print("Cart updated successfully!")
            print("=== END ADD_TO_CART DEBUG ===\n")
            return JsonResponse({'message': 'Cart updated successfully!'}, status=201)

        except Exception as e:
            print(f"Exception in add_to_cart: {str(e)}")
            print(traceback.format_exc())
            print("=== END ADD_TO_CART DEBUG (ERROR) ===\n")
            return JsonResponse({'error': str(e)}, status=500)

def cart_count(request):
    cart_length = Cart.objects.count() 
    return JsonResponse(cart_length, safe=False)

@api_view(['GET'])
def total_cart(request):
    try:
        carts = Cart.objects.filter(disabled=False)
        data = [cart.as_dict() for cart in carts]
        return JsonResponse(data, safe=False)
    except Exception as e:
        print(f"Error in total_cart: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def cart_delete(request, cart_id):
    if request.method == 'DELETE':
        cart_item = get_object_or_404(Cart, id=cart_id)
        cart_item.delete() 
        return JsonResponse({"message": "Item deleted successfully"}, status=200)

    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def cart_status(request, cart_id):
    if request.method == 'PATCH':
        try:
            cart_item = get_object_or_404(Cart, id=cart_id)

            # Toggle status
            cart_item.status = not cart_item.status
            cart_item.save()

            return JsonResponse({
                "message": "Status toggled successfully",
                "status": cart_item.status
            })
        except Exception as e:
            print("Error in toggle_status:", e)  # check console
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def cart_qty_add(request, cart_id):
    if request.method == 'PATCH':
        try:
            cart_item = get_object_or_404(Cart, id=cart_id)

            # Parse JSON safely


            try:
                data = json.loads(request.body)
            except Exception:
                return JsonResponse({"error": "Invalid JSON"}, status=400)

            # Accept numeric string or int; default delta is 1
            try:
                delta = int(data.get('add_qty', 1))
            except Exception:
                delta = 1

            cart_item.qty = cart_item.qty + delta
            cart_item.save()

            return JsonResponse({"message": "Qty updated successfully", "qty": cart_item.qty})
        except Exception as e:
            print("Error in add_qty:", e)  # Check console for details
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def cart_qty_sub(request, cart_id):
    if request.method == 'PATCH':
        try:
            cart_item = get_object_or_404(Cart, id=cart_id)

            # Parse JSON safely


            try:
                data = json.loads(request.body)
            except Exception:
                return JsonResponse({"error": "Invalid JSON"}, status=400)

            try:
                delta = int(data.get('sub_qty', 1))
            except Exception:
                delta = 1

            # Prevent quantity going below 1
            cart_item.qty = max(cart_item.qty - delta, 1)
            cart_item.save()

            return JsonResponse({"message": "Qty decreased successfully", "qty": cart_item.qty})
        except Exception as e:
            print("Error in sub_qty:", e)
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Method not allowed"}, status=405)

@api_view(['POST'])
def payment_checkout(request):
    try:
        # Process the incoming data (this is just an example)
        phoneNumber = request.data.get('phoneNumber')
        email = request.data.get('email')
        fullName = request.data.get('fullName')
        address = request.data.get('address')
        instructions = request.data.get('instructions', 'No instructions.')
        currency = request.data.get('currency', 'usd')
        total_cart_check = request.data.get('total_cart_check', [])
        totalPlusShip_usd = request.data.get('totalPlusShip_usd' )
        totalPlusShip_kh = request.data.get('totalPlusShip_kh' )
        product_id = request.data.get('product_id')
        getSelectedCartItems = request.data.get('getSelectedCartItems')

        # Load Telegram credentials from .env with fallback defaults
        chat_id = os.getenv('TELEGRAM_CHAT_ID', '1576176721')
        token = os.getenv('TELEGRAM_BOT_TOKEN', '8300831905:AAHmRGaoTfLMpWx_HKqTbVYZqgJIkWf-wW0')
        
        print(f"\n=== TELEGRAM PAYMENT CHECKOUT ===")
        print(f"Chat ID: {chat_id}")
        print(f"Token loaded: {token[:20]}..." if token else "No token")

        cart_length = len(total_cart_check)

        cart_list = []

        for i in range(cart_length):
            cart_list.append([
                total_cart_check[i]['name'],
                total_cart_check[i]['qty'],
                total_cart_check[i]['price']
            ])

        table = tabulate(cart_list, ["Item", "Qty", "Price"], tablefmt="fancy_outline")

        message = (f"<b>Order Details:</b>\n"
                   f"<pre>{table}</pre>\n\n"
                   f"<b>Shipping Details:</b>\n"
                   f"<b>Full Name:</b> {fullName}\n"
                   f"<b>Phone Number:</b> {phoneNumber}\n"
                   f"<b>Email:</b> {email}\n"
                   f"<b>Address:</b> {address}\n"
                   f"<b>Special Instructions:</b> {instructions}\n\n"
                   f"<b>Payment Info:</b>\n"
                   f"<b>Currency:</b> {currency}\n"
                   f"<b>USD:</b> {totalPlusShip_usd}\n"
                   f"<b>KHM:</b> {totalPlusShip_kh}"
                   )

        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={quote_plus(message)}&parse_mode=html"
        print(f"Sending Telegram request to: {url[:80]}...")
        
        r = requests.get(url)
        print(f"Telegram response status: {r.status_code}")
        print(f"Telegram response: {r.text}")
        print("=== END TELEGRAM PAYMENT CHECKOUT ===\n")

        if r.status_code != 200:
            return JsonResponse({
                "error": "Failed to send message to Telegram"
            }, status=500)


        # Example response
        return JsonResponse({
            'message': 'Your order processed successfully',
            'getSelectedCartItems' : getSelectedCartItems,
        }, status=200)

    except Exception as e:
        # If an error occurs, return an error message and log traceback
        print(f"Exception in payment_checkout: {str(e)}")
        print(traceback.format_exc())
        print("=== END TELEGRAM PAYMENT CHECKOUT (ERROR) ===\n")
        return JsonResponse({'error': str(e)}, status=400)


####### add cart to db

@api_view(['GET'])
def cart_detail(request):
    try:
        carts = Cart.objects.all()
        data = [item.as_dict() for item in carts]
        return JsonResponse(data, safe=False)
    except Exception as e:
        print(f"Error in cart_detail: {str(e)}")
        print(traceback.format_exc())
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['GET'])
def order_detail(request):
    try:
        order_details = OrderDetail.objects.all()
        data = [item.as_dict() for item in order_details]
        return JsonResponse(data, safe=False)
    except Exception as e:
        print(f"Error in order_detail: {str(e)}")
        print(traceback.format_exc())
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['POST'])
def add_cart_checkout(request):
    try:
        data = request.data.get('checkout')

        for item in data:
            product_id = item.get('p_id')

            existing_item = OrderDetail.objects.filter(product_id=product_id).first()

            if existing_item:
                # If found, just increase qty
                existing_item.quantity += int(item.get('qty'))
                existing_item.save()
            else:
                OrderDetail.objects.create(
                    quantity=item.get('qty'),
                    price=item.get('price'),
                    product_id=product_id
                )

        return JsonResponse({
            "message": "success",
            "data": data,
        }, status=201)

    except Exception as e:
        print("Exception in add_cart_checkout:", str(e))
        print(traceback.format_exc())
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['POST'])
def add_customer_info(request):
    try :
        res = request.data

        phoneNumber = res.get('phoneNumber')
        email = res.get('email')
        fullName = res.get('fullName')
        address = res.get('address')
        totalAmount = res.get('totalAmount')
        currencyType = res.get('currencyType')
        carts = res.get('cart')
        cartDetail = res.get('cartDetail')

        # Validate required fields
        if not all([phoneNumber, fullName, address, totalAmount, currencyType]):
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        # Ensure totalAmount is a number
        totalAmount = float(totalAmount)

        # check_out in here used to reference ID in table order
        check_out = Checkout.objects.create(
            phone=phoneNumber,
            email=email,
            fullname=fullName,
            address=address,
            total=totalAmount,
            currency=currencyType,
        )

        # insert into cart_checkout table
        for item in carts:
            CartCheckout.objects.create(
                cart_id=item,
                checkout_id=check_out.id
            )

        # insert into order
        for item in cartDetail:
            Order.objects.create(
                status='pending',
                checkout_id=check_out.id,
                orderdetail_id=item
            )

        return JsonResponse({
            'message': 'Customer info added successfully',
            'total' : totalAmount,
            'currency': currencyType,
        }, status=201)

    except Exception as e:
        print("Exception in add_customer_info:", str(e))
        print(traceback.format_exc())
        return JsonResponse({'error': str(e)}, status=500)

def orderId(request):
    try:
        # Get the last order with 'pending' status
        last_order = Order.objects.filter(status='pending').last()

        if last_order:
            return JsonResponse({
                    'id': last_order.id,
                    'status': last_order.status
            })
        else:
            return JsonResponse({'message': 'No pending orders found'}, status=404)

    except Exception as e:
        print("Exception in payment_success:", str(e))
        print(traceback.format_exc())
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['POST'])
def payment_success(request):
    try :
        if request.method == 'POST':
            # Use DRF request.data instead of reading request.body
            data = request.data

            from_account_id = data.get('from_account_id')
            description = data.get('description')
            currency_type = data.get('currency_type')
            amount = data.get('amount')
            formattedDate = data.get('formattedDate')
            hash = data.get('hash')
            status = data.get('status')
            order_id = data.get('order_id')
            cart_ids = data.get('cart_id')

            Payment.objects.create(
                from_account_id=from_account_id,
                description=description,
                currency_type=currency_type,
                amount=amount,
                create_date=formattedDate,
                hash=hash,
                status=status,
                order_id=order_id
            )

            # delete cart items
            # Cart.objects.filter(id__in=cart_ids).delete() 

            order_item = Order.objects.filter(id=order_id).first()
            if order_item:
                order_item.status = 'paid'
                order_item.save()

            return JsonResponse({
                'status' : 'ok',
                'payment' :'Completed',
                'redirect' : '/success',
            })
        else :
            return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

    except Exception as e:
        print("Exception in payment_success:", str(e))
        print(traceback.format_exc())
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['POST'])
def telegram_sender(request):
    try:
        if request.method == 'POST':
            # Use request.data provided by DRF
            data = request.data
            cart_ids = data.get('cart_id')

            print(f"\n=== TELEGRAM SENDER ===")
            print(f"Cart IDs received: {cart_ids}")

            # Check if cart_ids is not empty or None
            if not cart_ids:
                print("ERROR: No cart_id provided or cart_id is empty")
                print("=== END TELEGRAM SENDER (ERROR) ===\n")
                return JsonResponse({'error': 'No cart_id provided or cart_id is empty'}, status=400)

            # Fetch the cart items
            cart_items = Cart.objects.filter(id__in=cart_ids) # Corrected line: using filter

            # If no items found, handle that case
            if not cart_items:
                print(f"ERROR: No cart items found for cart_ids: {cart_ids}")
                print("=== END TELEGRAM SENDER (ERROR) ===\n")
                return JsonResponse({'error': 'No cart items found for the provided cart_id(s)'}, status=404)

            # Build cart items data for both Telegram and email
            cart_items_data = [
                {
                    'id': item.id,
                    'name': item.name,
                    'price': item.price,
                    'qty': item.qty
                }
                for item in cart_items
            ]

            # Get Telegram credentials from .env
            chat_id = os.getenv('TELEGRAM_CHAT_ID', '1576176721')
            token = os.getenv('TELEGRAM_BOT_TOKEN', '8300831905:AAHmRGaoTfLMpWx_HKqTbVYZqgJIkWf-wW0')

            print(f"Chat ID: {chat_id}")
            print(f"Token loaded: {token[:20]}..." if token else "No token")
            print(f"Items to send: {len(cart_items_data)}")

            # Build Telegram message with cart items
            cart_list = [[item['name'], item['qty'], item['price']] for item in cart_items_data]
            table = tabulate(cart_list, ["Item", "Qty", "Price"], tablefmt="fancy_outline")

            message = (f"<b>Order Summary:</b>\n"
                      f"<pre>{table}</pre>\n"
                      f"<b>Total Items:</b> {len(cart_items_data)}")

            url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={quote_plus(message)}&parse_mode=html"
            print(f"Sending Telegram message...")
            
            r = requests.get(url)
            print(f"Telegram response status: {r.status_code}")
            print(f"Telegram response: {r.text}")

            if r.status_code != 200:
                print("ERROR: Failed to send Telegram message")
                print("=== END TELEGRAM SENDER (ERROR) ===\n")
                return JsonResponse({'error': 'Failed to send message to Telegram'}, status=500)

            # Send email to customer
            from_email = Checkout.objects.all().last().email if Checkout.objects.exists() else 'noreply@store.com'
            your_message = 'Thank You for Your Order!'

            try:
                send_mail(
                    subject='Thank You for Your Order - SU Store',
                    message=str(your_message),
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[from_email],
                    fail_silently=False,
                )
                print(f"Email sent to {from_email}")
            except Exception as email_error:
                print(f"WARNING: Failed to send email: {email_error}")

            print("SUCCESS: Telegram message and order confirmed")
            print("=== END TELEGRAM SENDER ===\n")

            return JsonResponse({
                'status': 'ok',
                'message': 'Order sent to Telegram and email',
                'cart_items': cart_items_data,
            })
        else:
            return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

    except Exception as e:
        print(f"Exception in telegram_sender: {str(e)}")
        print(traceback.format_exc())
        print("=== END TELEGRAM SENDER (ERROR) ===\n")
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['POST'])
def update_disabled_cart(request):
    try:
        # Use DRF request.data for consistent parsing
        data = request.data or {}

        cart_id = data.get('cart_id')

        orderid = None
        if cart_id is not None:
            try:
                orderid = Order.objects.get(id=cart_id)
            except Order.DoesNotExist:
                orderid = None

        return JsonResponse({
            'cart_id': cart_id
        })

    except Exception as e:
        print("ERROR in update_disabled_cart:", str(e))   # Debug
        print(traceback.format_exc())
        return JsonResponse({'error': str(e)}, status=500)