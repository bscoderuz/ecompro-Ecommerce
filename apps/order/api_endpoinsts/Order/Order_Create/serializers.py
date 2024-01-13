from rest_framework import serializers

from apps.order.models.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity', 'item_price', ]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            'full_name',
            'phone_number',
            'email',
            'product',
            'items',
            'delivery_type',
            'payment_method',
            'city',
            'region',
            'address',
            'level',
            'delivery_date',
        ]
