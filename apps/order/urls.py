from django.urls import path
from . import api_endpoinsts as views

urlpatterns = [
    path('list/', views.OrderListAPIView.as_view(), name="order_list"),
    path('retrieve/<int:pk>/', views.OrderRetrieveAPIView.as_view(), name='order_retrieve')

]
