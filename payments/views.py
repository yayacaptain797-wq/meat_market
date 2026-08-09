from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required


import requests

from cart.views import get_user_cart
from orders.models import Order, OrderItem

@login_required
def initialize_payment(request):

    cart = get_user_cart(request)

    email = request.user.email

    if not email:
        email = "customer@test.com"


    total = 0

    for item in cart.items.all():
        total += item.subtotal()


    amount = int(total * 100)


    url = "https://api.paystack.co/transaction/initialize"


    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json",
    }


    data = {
        "email": email,
        "amount": amount,
        "callback_url": request.build_absolute_uri(
            "/payments/verify/"
        ),
    }


    response = requests.post(
        url,
        json=data,
        headers=headers
    )


    result = response.json()


    if result.get("status"):

        return redirect(
            result["data"]["authorization_url"]
        )


    return render(
        request,
        "payment_failed.html"
    )
    from django.http import HttpResponse
@login_required
def verify_payment(request):

    reference = request.GET.get("reference")

    if not reference:
        return render(
            request,
            "payment_failed.html"
        )

    url = f"https://api.paystack.co/transaction/verify/{reference}"

    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
    }

    response = requests.get(
        url,
        headers=headers
    )

    result = response.json()

    if result.get("status") and result["data"]["status"] == "success":

        cart = get_user_cart(request)

        order = Order.objects.filter(
            user=request.user,
            status="Pending"
        ).last()

        if order:

            order.status = "Paid"
            order.payment_reference = reference
            order.save()

            for item in cart.items.all():

                OrderItem.objects.get_or_create(
                    order=order,
                    product=item.product,
                    defaults={
                        "quantity": item.quantity,
                        "price": item.product.price,
                    }
                )

                item.product.stock -= item.quantity

                if item.product.stock <= 0:
                    item.product.stock = 0
                    item.product.is_available = False

                item.product.save()

            cart.items.all().delete()

        return render(
            request,
            "payment_success.html"
        )

    return render(
        request,
        "payment_failed.html"
    )