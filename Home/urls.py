from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('productdetails', views.productdetails, name='product_details'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('shop', views.shop, name='shop'),
    path('checkout', views.checkout, name='checkout'),
    path('cart', views.cart, name='cart'),

    path('send_email', views.email_sender, name='send_email'),
    path('addtocart/', views.add_to_cart, name='addtocart'),
    path('cartcount',views.cart_count,name='cartcount'),
    path('total_cart', views.total_cart, name='total_cart'),
    path('cart/status/<int:cart_id>', views.cart_status, name='cart_status'),
    path('cart/delete/<int:cart_id>',views.cart_delete,name='cart_delete'),
    path('cart/qty/add/<int:cart_id>',views.cart_qty_add,name='cart_qty_add'),
    path('cart/qty/sub/<int:cart_id>', views.cart_qty_sub, name='cart_qty_sub'),
    # path('payment/', views.payment_checkout, name='payment_checkout'),

    path('fetchproducts', views.fetchproducts, name='fetchproducts'),

    path('qr_generate/', views.qr_generate, name='qr_generate'),
    path('payment/', views.payment, name='payment'),
    path('success', views.success, name='success'),
    path('check_payment_status/',views.check_payment_status,name='check_payment_status'),


    path('cart/cart_detail',views.cart_detail,name='cart_detail'),
    path('cart/order_detail',views.order_detail,name='order_detail'),
    path('add_cart_checkout/', views.add_cart_checkout, name='add_cart_checkout'),
    path('add_customer_info/', views.add_customer_info, name='add_customer_info'),

    path('orderId', views.orderId, name='orderId'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('update_disabled_cart/',views.update_disabled_cart, name='update_disabled_cart'),

    path('telegram_sender/',views.telegram_sender,name='telegram'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


















