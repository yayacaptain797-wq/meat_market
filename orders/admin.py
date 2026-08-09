from django.contrib import admin

from .models import Order, OrderItem, OrderNotification


class OrderItemInline(admin.TabularInline):

    model = OrderItem
    extra = 0



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "full_name",
        "phone",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "full_name",
        "phone",
        "user__username",
    )

    readonly_fields = (
        "created_at",
    )

    inlines = [
        OrderItemInline,
    ]



@admin.register(OrderNotification)
class OrderNotificationAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "order",
        "message",
        "is_read",
        "created_at",
    )

    list_filter = (
        "is_read",
        "created_at",
    )