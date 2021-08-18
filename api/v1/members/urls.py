from django.urls import path
from .import views

urlpatterns = [
    path('list/', views.MemberList.as_view(), name='member_list'),
    path('', views.MemberCreate.as_view(), name='member_create'),
    path('<str:pk>/', views.MemberDetail.as_view(), name='member_detail'),
]
