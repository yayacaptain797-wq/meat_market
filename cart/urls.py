from django.urls import path

from .views import (
    cart_detail,
    add_to_cart,
    increase_quantity,
    decrease_quantity,
    remove_item,
    checkout,
)


urlpatterns = [

    path(
        "",
        cart_detail,
        name="cart_detail"
    ),

    path(
        "add/<int:id>/",
        add_to_cart,
        name="add_to_cart"
    ),

    path(
        "increase/<int:id>/",
        increase_quantity,
        name="increase_quantity"
    ),

    path(
        "decrease/<int:id>/",
        decrease_quantity,
        name="decrease_quantity"
    ),

    path(
        "remove/<int:id>/",
        remove_item,
        name="remove_item"
    ),

    path(
        "checkout/",
        checkout,
        name="checkout"
    ),

]