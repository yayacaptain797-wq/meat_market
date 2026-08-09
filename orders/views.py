from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Order, OrderNotification
from xhtml2pdf import pisa

from .models import Order


@login_required
def order_history(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        "orders/order_history.html",
        {
            "orders": orders
        }
    )


@login_required
def order_invoice(request, id):

    order = get_object_or_404(
        Order,
        id=id,
        user=request.user
    )

    return render(
        request,
        "orders/invoice.html",
        {
            "order": order
        }
    )


@login_required
def download_invoice(request, id):

    order = get_object_or_404(
        Order,
        id=id,
        user=request.user
    )

    template = get_template(
        "orders/invoice_pdf.html"
    )

    html = template.render(
        {
            "order": order
        }
    )

    response = HttpResponse(
        content_type="application/pdf"
    )

    response["Content-Disposition"] = (
        f"attachment; filename=invoice_{order.id}.pdf"
    )

    pisa.CreatePDF(
        html,
        dest=response
    )

    return response

@login_required
def notifications(request):

    notifications = OrderNotification.objects.filter(
        user=request.user
    ).order_by("-created_at")


    return render(
        request,
        "orders/notifications.html",
        {
            "notifications": notifications
        }
    )