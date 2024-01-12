from rest_framework import serializers

from apps.order.models.models import Order


class OrderListSerializer(serializers.ModelSerializer):
    quantity = serializers.SerializerMethodField()

    def get_quantity(self, instance):
        return instance.items.count

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
            "quantity",
            'delivery_date',
        ]
        depth = 1
