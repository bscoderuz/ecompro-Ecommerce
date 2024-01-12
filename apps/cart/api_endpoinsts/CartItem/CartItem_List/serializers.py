from rest_framework import serializers
from apps.cart.models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity', 'item_price']
        ref_name = 'CartItemList'

