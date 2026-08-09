from django.urls import path
from .views import initialize_payment, verify_payment

urlpatterns = [
    path(
        "pay/",
        initialize_payment,
        name="pay"
    ),

    path(
        "verify/",
        verify_payment,
        name="verify_payment"
    ),
]