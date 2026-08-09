from django.db import models
from django.contrib.auth.models import User
from inventory.models import Product


class Cart(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"{self.user.username} Cart"


class CartItem(models.Model):

    cart = models.ForeignKey(
        Cart,
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

    def subtotal(self):

        if self.product.discount_price:
            return self.product.discount_price * self.quantity

        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name