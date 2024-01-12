from django.db import models
from django.db.models import Sum

from apps.product.models import Product
from apps.common.models import TimeStampedModel


class Cart(TimeStampedModel):
    user = models.OneToOneField(to='users.User', related_name='cart', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return f"{self.user.username}'s cart"

    @property
    def get_price(self):
        return self.items.aggregate(total=Sum('item_price'))['total']


class CartItem(TimeStampedModel):
    cart = models.ForeignKey(
        to='Cart', related_name='items', on_delete=models.CASCADE, blank=True, null=True
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    item_price = models.DecimalField(max_digits=24, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.product} - Quantity: {self.quantity} - Item Price: {self.item_price}"

    class Meta:
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItems'
