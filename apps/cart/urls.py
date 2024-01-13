from django.urls import path
from . import api_endpoinsts as views

urlpatterns = [
    path('cart-items/create/', views.CartItemCreateAPIView.as_view(), name='cartitem-create'),
    path('cart-items/list/<int:cart_id>/', views.CartItemListAPIView.as_view(), name='cartitem-list'),
    path('cart-items/delete/<int:pk>/', views.CartItemDeleteAPIView.as_view(), name='cartitem-delete'),

]
