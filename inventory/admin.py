from django.shortcuts import render
from .models import Product, Category
from django.contrib import admin
from .models import Category, Product, ProductImage, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "price",
        "stock",
        "is_available",
        "is_featured",
    )

    list_filter = (
        "category",
        "is_available",
        "is_featured",
    )

    search_fields = (
        "name",
        "sku",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    inlines = [
        ProductImageInline,
    ]



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "product",
        "user",
        "rating",
        "created_at",
    )

    list_filter = (
        "rating",
    )
    


def shop(request):

    products = Product.objects.filter(
        is_available=True
    )

    categories = Category.objects.all()


    context = {
        "products": products,
        "categories": categories,
    }


    return render(
        request,
        "shop.html",
        context
    )