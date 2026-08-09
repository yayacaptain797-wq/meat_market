from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)


    def __str__(self):
        return self.name



class Product(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    name = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
    unique=True,
    blank=True,
    null=True
)

    sku = models.CharField(
    max_length=50,
    unique=True,
    blank=True,
    null=True
)
    

    description = models.TextField(
        blank=True
    )


    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )


    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )


    image = models.ImageField(
        upload_to="products/"
    )


    stock = models.PositiveIntegerField(
        default=0
    )


    is_available = models.BooleanField(
        default=True
    )


    is_featured = models.BooleanField(
        default=False
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )



    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)



    def __str__(self):
        return self.name



class ProductImage(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(
        upload_to="products/gallery/"
    )


    def __str__(self):
        return self.product.name



class Review(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    rating = models.PositiveIntegerField(
        choices=[
            (1, "1 Star"),
            (2, "2 Stars"),
            (3, "3 Stars"),
            (4, "4 Stars"),
            (5, "5 Stars"),
        ]
    )

    comment = models.TextField()


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"{self.product} - {self.rating}"