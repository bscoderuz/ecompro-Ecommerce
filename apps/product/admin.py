from django.contrib import admin
from .models.models import Product, ProductImage, Category


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)