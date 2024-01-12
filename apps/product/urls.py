from django.urls import path
from . import api_endpoints as views

urlpatterns = [
    path('category/list/', views.CategoryListAPIView.as_view(), name='category_list'),
    path('products/list/', views.ProductListAPIView.as_view(), name='product_list'),
    path('products/create/', views.ProductCreateAPIView.as_view(), name='product_create'),
    path('products/<int:pk>/', views.ProductRetrieveAPIView.as_view(), name='product_retrieve'),
]
