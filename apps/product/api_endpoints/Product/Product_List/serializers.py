from rest_framework import serializers
from apps.product.models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        ref_name = "ProductImage"
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'images', 'price', 'active']
        depth = 1
