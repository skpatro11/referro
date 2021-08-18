from django.urls import path, include

urlpatterns = [
    path('programs/', include('api.v1.programs.urls')),
    path('members/', include('api.v1.members.urls')),
    path('orders/', include('api.v1.orders.urls')),
]
