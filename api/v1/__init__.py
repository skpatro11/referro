from django.urls import path, include

urlpatterns = [
    path('programs/', include('api.v1.programs.urls'))
]
