from django.urls import path
from .import views

urlpatterns = [
    path('list/', views.OrderList.as_view(), name='order_list'),
    path('', views.OrderCreate.as_view(), name='order_create'),
    path('<int:pk>/', views.OrderDetail.as_view(), name='order_detail'),
]
