from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProgramList.as_view(), name='member_list'),
    path('<str:pk>/', views.ProgramDetail.as_view(), name='member_detail'),
    path('<str:pk>/access_token/', views.ProgramAccessToken.as_view(), name='generate_access_token')
]
