from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from .serializers import MemberSerializer, MemberProgramSerializer
from .permissions import IsOwner
from api.v1.exceptions import ProgramNotFound, ProgramIdNotFound
from members.models import Member
from programs.models import Program

class MemberList(generics.ListAPIView):
    serializer_class = MemberProgramSerializer
    queryset = Member.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        program_id = self.request.query_params.get('program_id')
        if not program_id:
            raise ProgramIdNotFound
        try:
            program = Program.objects.get(id=program_id)
            return program.members.all()
        except Program.DoesNotExist:
            raise ProgramNotFound


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
