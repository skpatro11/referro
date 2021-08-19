from django.urls import path, include

urlpatterns = [
    path('overview/', include('api.v1.overview.urls')),
    path('programs/', include('api.v1.programs.urls')),
    path('members/', include('api.v1.members.urls')),
    path('orders/', include('api.v1.orders.urls')),
]
