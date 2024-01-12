from django.urls import path
from . import api_endpoinsts as views

urlpatterns = [
    path('api/cart-items/create/<int:cart_id>/', views.CartItemCreateAPIView.as_view(), name='cartitem-create'),
    path('api/cart-items/list/<int:cart_id>/', views.CartItemListAPIView.as_view(), name='cartitem-list'),
    path('api/cart-items/delete/<int:pk>/', views.CartItemDeleteAPIView.as_view(), name='cartitem-delete'),

]
