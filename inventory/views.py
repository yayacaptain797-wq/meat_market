from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def home(request):

    products = Product.objects.all()

    return render(
        request,
        "home.html",
        {
            "products": products
        }
    )


def shop(request):

    products = Product.objects.filter(
        is_available=True
    )

    categories = Category.objects.all()

    return render(
        request,
        "shop.html",
        {
            "products": products,
            "categories": categories,
        }
    )


def product_detail(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    return render(
        request,
        "product_detail.html",
        {
            "product": product
        }
    )