from django.urls import path
from .import views

urlpatterns = [
    path('', views.ProgramList.as_view(), name='program_list'),
    path('<str:program_id>/', views.ProgramDetail.as_view(), name='program_detail'),
    path('<str:pk>/members/', views.ProgramMemberView.as_view(), name='program_members'),
    path('<str:program_id>/members/<str:pk>/', views.ProgramMemberDetailView.as_view(), name='program_members_detail'),
    path('<str:program_id>/orders/', views.ProgramOrdersListView.as_view(), name='program_orders'),
    path('<str:program_id>/orders/<int:pk>/', views.ProgramOrdersDetailView.as_view(), name='program_orders_detail'),
    path('<str:program_id>/orders/<int:pk>/claim/', views.ProgramOrderDetailViewClaim.as_view(), name='program_orders_detail_claim'),
    path('access_token/<str:program_id>/', views.access_token, name='access_token')
]
