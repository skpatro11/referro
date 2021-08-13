from django.urls import path
from .import views

urlpatterns = [
    path('programs/<str:pk>/', views.ProgramListView.as_view(), name='programs_detail'),
    path('programs/<str:pk>/members/', views.MemberListView.as_view(), name='members_list'),
    path('programs/<str:pk>/orders/', views.OrdersListView.as_view(), name='orders_list'),
    path('programs/<str:program_id>/members/<str:pk>/', views.MemberDetailView.as_view(), name='member_detail'),
    path('programs/<str:program_id>/orders/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
]
