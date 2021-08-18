from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework import permissions
from .permissions import IsOwner
from programs.models import Program
from .serializers import ProgramSerializer
from django.http import JsonResponse


class ProgramList(generics.ListCreateAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = Program.objects.all()
        queryset = queryset.filter(owner=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProgramDetail(generics.RetrieveDestroyAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner)
