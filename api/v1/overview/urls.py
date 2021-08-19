from django.urls import path
from .import views

urlpatterns = [
    path('programs/detail/count', views.programs_detail_count, name='programs_detail_count')
]
