from rest_framework import serializers

from apps.order.models.models import Order


class OrderRetrieveSerializer(serializers.ModelSerializer):
    quantity = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'full_name',
            'phone_number',
            'email',
            'product',
            'delivery_type',
            'payment_method',
            'city',
            'region',
            'address',
            'level',
            'delivery_date',
        ]
        depth = 1
