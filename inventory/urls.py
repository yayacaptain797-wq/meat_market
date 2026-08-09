from django.urls import path
from .views import home, shop, product_detail

urlpatterns = [

    path(
        "",
        home,
        name="home"
    ),

    path(
        "shop/",
        shop,
        name="shop"
    ),

    path(
        "product/<int:id>/",
        product_detail,
        name="product_detail"
    ),
]