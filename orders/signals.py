from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order, OrderNotification


@receiver(post_save, sender=Order)
def create_order_notification(sender, instance, created, **kwargs):

    print("SIGNAL WORKING:", instance.id, instance.status)

    if not created:

        OrderNotification.objects.create(
            user=instance.user,
            order=instance,
            message=f"Your Order #{instance.id} status is now {instance.status}"
        )