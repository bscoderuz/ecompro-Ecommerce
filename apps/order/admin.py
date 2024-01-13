from django.contrib import admin

from apps.order.models.models import Order, OrderItem


class OrderItemInOrder(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone_number', 'product', 'delivery_type']
    list_display_links = ['id', 'full_name', 'phone_number']
    inlines = [OrderItemInOrder]



