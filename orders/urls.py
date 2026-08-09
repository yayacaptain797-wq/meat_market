from django.urls import path
from .views import order_history
from .views import (
    order_history,
    order_invoice,
    download_invoice
)
from .views import (
    order_history,
    order_invoice,
    download_invoice,
    notifications,
)

urlpatterns = [
    path(
        "history/",
        order_history,
        name="order_history"
    ),
    path(
    "invoice/<int:id>/",
    order_invoice,
    name="order_invoice"
),
path(
    "invoice/download/<int:id>/",
    download_invoice,
    name="download_invoice"
),
path(
    "notifications/",
    notifications,
    name="notifications"
),
]