from django.urls import path
from .import views

urlpatterns = [
    path('programs/detail/count', views.programs_detail_count, name='programs_detail_count'),
    path('programs/<str:program_id>/members/stats/', views.program_members_stats, name='members_stats'),
    path('programs/<str:program_id>/orders/stats/', views.program_orders_stats, name='orders_stats'),
]
