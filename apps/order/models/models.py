from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .choices import DELIVERY_TYPES, ORDER_STATUS
from apps.product.models import Product


class Order(models.Model):
    user = models.ForeignKey('users.User', related_name='orders', on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, related_name='order_products', on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=128)
    phone_number = PhoneNumberField(region='UZ')
    email = models.EmailField(blank=True, null=True)
    delivery_type = models.CharField(choices=DELIVERY_TYPES, max_length=1)
    payment_method = models.ForeignKey("PaymentType", related_name='orders', on_delete=models.SET_NULL,
                                       null=True, blank=True)
    final_price = models.DecimalField(max_digits=24, decimal_places=2, default=0)

    city = models.CharField(max_length=128, blank=True, null=True)
    region = models.CharField(max_length=128, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    level = models.CharField(max_length=128, blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=ORDER_STATUS, default='p')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"Order {self.id} by {self.user.username}" if self.user else f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey("order.Order", related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_item_products', on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()
    item_price = models.DecimalField(max_digits=24, decimal_places=2)

    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'

    def __str__(self):
        return f"{self.product.title} - {self.quantity} - {self.item_price}"


class PaymentType(models.Model):
    title = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Payment type'
        verbose_name_plural = 'Payment types'

    def __str__(self):
        return self.title
