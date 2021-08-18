from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from .serializers import MemberSerializer, MemberProgramSerializer
from .permissions import IsOwner
from members.models import Member

class MemberList(generics.ListAPIView):
    serializer_class = MemberProgramSerializer
    queryset = Member.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        programs = self.request.user.programs.all()
        queryset = None
        for program in programs:
            if queryset is None:
                queryset = program.members.all()
            else:
                queryset = queryset.union(program.members.all())
        return queryset


class MemberCreate(generics.CreateAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MemberProgramSerializer(instance)
        return Response(serializer.data)
