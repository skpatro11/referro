from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from .permissions import IsOwner
from programs.models import Program
from .serializers import ProgramSerializer


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


class ProgramAccessToken(generics.RetrieveAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.generate_access_token()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)