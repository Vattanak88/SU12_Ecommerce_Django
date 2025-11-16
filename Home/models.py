from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def as_dict(self):
        return {'id': self.id, 'name': self.name}


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()
    rate = models.DecimalField(max_digits=3, decimal_places=1)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return f"{self.name} - {self.price} USD"

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': str(self.price),
            'category': self.category.name,
            'image': self.image,
            'rate': str(self.rate),
            'discount_price': str(self.discount_price),
            'quantity': self.quantity
        }

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.URLField()
    qty = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.BooleanField(default=False)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="carts", null=True, blank=True)
    disabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'qty': self.qty,
            'status': self.status,
            'price': str(self.price) if self.price else None,
            'product_id': self.product.id if self.product else None,
            'disabled': self.disabled,
        }

class Checkout(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.fullname}"

    def as_dict(self):
        return {
            'id': self.id,
            'fullname': self.fullname,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'total': str(self.total),
            'currency': self.currency
        }

class CartCheckout(models.Model):
    id = models.AutoField(primary_key=True)
    checkout = models.ForeignKey('Checkout', on_delete=models.CASCADE, related_name="cart_checkouts",null=True, blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name="checkouts",null=True, blank=True)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50, default="pending")
    checkout = models.ForeignKey('Checkout', on_delete=models.CASCADE, related_name="orders")
    orderdetail = models.ForeignKey('OrderDetail', on_delete=models.CASCADE, related_name="orders", null=True, blank=True)

    def __str__(self):
        return f"Order for {self.checkout.fullname} - Status: {self.status}"

    def as_dict(self):
        return {
            'id': self.id,
            'checkout': self.checkout.as_dict(),
            'status': self.status
        }

class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_details")
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def total(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.product.name} - {self.quantity} items"

    def as_dict(self):
        return {
            'id': self.id,
            'product': self.product.name,
            'quantity': self.quantity,
            'price': str(self.price),
            'total_price': str(self.total())
        }

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    from_account_id = models.CharField(max_length=255)
    description = models.TextField()
    currency_type = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    create_date = models.DateTimeField(auto_now_add=True)
    hash = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name="payments")



    def __str__(self):
        return f"Payment #{self.id} for Order #{self.order.id}"

    def as_dict(self):
        return {
            'id': self.id,
            'from_account_id': self.from_account_id,
            'description': self.description,
            'currency_type': self.currency_type,
            'amount': str(self.amount),
            'create_date': self.create_date,
            'hash': self.hash,
            'status': self.status,
            'order_id': self.order.id,

        }

class Feature(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    image = models.URLField()

    def __str__(self):
        return f"{self.title}"

    def as_dict(self):
        return {
            'title': self.title,
            'image': self.image
        }

class Slider(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    collection = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    description = models.TextField()
    image = models.URLField()
    status = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.title}"

    def as_dict(self):
        return {
            'title': self.title,
            'collection': self.collection,
            'year': self.year,
            'description': self.description,
            'image': self.image,
            'status': self.status,
        }
