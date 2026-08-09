
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart
from inventory.models import Product

class Order(models.Model):

    STATUS_CHOICES = [
    ("Pending", "Pending"),
    ("Paid", "Paid"),
    ("Processing", "Processing"),
    ("Delivered", "Delivered"),
    ("Cancelled", "Cancelled"),
]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=20
    )

    address = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )
    payment_reference = models.CharField(
    max_length=100,
    blank=True,
    null=True,
    unique=True
)

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"Order {self.id}"
class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        related_name="items",
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )


    @property
    def subtotal(self):

        return self.price * self.quantity


    def __str__(self):

        return self.product.name
class OrderNotification(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )

    message = models.TextField()

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.message