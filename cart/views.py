from orders.models import Order
from orders.forms import OrderForm

from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required

from inventory.models import Product
from .models import Cart, CartItem
from orders.models import OrderItem



def get_user_cart(request):

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    return cart



@login_required
def add_to_cart(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    cart = get_user_cart(request)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        cart_item.quantity += 1

    cart_item.save()

    return redirect("cart_detail")



@login_required
def cart_detail(request):

    cart = get_user_cart(request)

    return render(
        request,
        "cart_detail.html",
        {
            "cart": cart
        }
    )



@login_required
def increase_quantity(request, id):

    item = get_object_or_404(
        CartItem,
        id=id
    )

    item.quantity += 1
    item.save()

    return redirect("cart_detail")



@login_required
def decrease_quantity(request, id):

    item = get_object_or_404(
        CartItem,
        id=id
    )

    if item.quantity > 1:
        item.quantity -= 1
        item.save()

    return redirect("cart_detail")



@login_required
def remove_item(request, id):

    item = get_object_or_404(
        CartItem,
        id=id
    )

    item.delete()

    return redirect("cart_detail")

@login_required
def checkout(request):

    cart = get_user_cart(request)

    if request.method == "POST":

        form = OrderForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)

            order.user = request.user
            order.cart = cart

            order.save()

            return redirect("pay")


    else:

        form = OrderForm()


    return render(
        request,
        "checkout.html",
        {
            "form": form,
            "cart": cart,
        }
    )