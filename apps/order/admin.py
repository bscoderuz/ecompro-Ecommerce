from django.contrib import admin
from apps.order.models.models import Order, OrderItem, PaymentType

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(PaymentType)
