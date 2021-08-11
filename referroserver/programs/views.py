import uuid
from django.http import Http404
from rest_framework import generics, serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner, IsOwnerAndIsProgram
from .models import Program
from .serializers import ProgramSerializer
from members.serializers import MemberSerializer
from members.models import Member
from orders.serializers import OrderSerializer
from orders.models import Order
from rest_framework.pagination import PageNumberPagination


class ProgramList(generics.ListCreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        programs = self.queryset.filter(owner=self.request.user)
        return programs

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProgramSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)


class ProgramDetail(APIView):
    permission_classes = (IsAuthenticated, IsOwner)

    def get_object(self, program_id):
        try:
            program = Program.objects.get(id=program_id)
            self.check_object_permissions(self.request, program)
            return program
        except Program.DoesNotExist:
            return Response({'detail': 'Program not found!'}, status=status.HTTP_404_NOT_FOUND)
            # return Http404

    def get(self, request, program_id, format=None):
        program = self.get_object(program_id)
        serializer = ProgramSerializer(program)
        return Response(serializer.data)

    def put(self, request, program_id, format=None):
        program = self.get_object(program_id)
        serializer = ProgramSerializer(program, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProgramMemberView(generics.ListCreateAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self, pk):
        try:
            program = Program.objects.get(pk=pk)
            self.check_object_permissions(self.request, program)
            members = Member.objects.filter(program=program)
            return members
        except Program.DoesNotExist:
            raise Http404

    def list(self, request, pk):
        queryset = self.get_queryset(pk)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, pk):
        try:
            program = Program.objects.get(pk=pk)
            self.check_object_permissions(self.request, program)

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer, program)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Program.DoesNotExist:
            return Response({'detail': 'Program not found!'}, status=status.HTTP_404_NOT_FOUND)

    def perform_create(self, serializer, program):
        serializer.save(program=program)
        return super().perform_create(serializer)


class ProgramMemberDetailView(APIView):
    permission_classes = (IsAuthenticated, IsOwner)

    def get_program(self, program_id):
        try:
            program = Program.objects.get(id=program_id)
            self.check_object_permissions(self.request, program)
            return program
        except Program.DoesNotExist:
            return Response(data={'detail': 'Program Does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def get_object(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, program_id, pk, format=None):
        program = self.get_program(program_id)
        member = self.get_object(pk)
        if not member.program.id == program_id:
            return Response({'detail': 'Request Denied'}, status=status.HTTP_403_FORBIDDEN)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def put(self, request, program_id, pk, format=None):
        program = self.get_program(program_id)
        member = self.get_object(pk)
        if not member.program.id == program_id:
            return Response({'detail': 'Request Denied'}, status=status.HTTP_403_FORBIDDEN)
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, program_id, pk, format=None):
        program = self.get_program(program_id)
        member = self.get_object(pk)
        if not member.program.id == program_id:
            return Response({'detail': 'Request Denied'}, status=status.HTTP_403_FORBIDDEN)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProgramOrdersListView(generics.ListAPIView, PageNumberPagination):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    queryset = Order.objects.all()
    # pagination_class = PageNumberPagination

    def get_program(self, program_id):
        try:
            program = Program.objects.get(id=program_id)
            self.check_object_permissions(self.request, program)
            return program
        except Program.DoesNotExist:
            return Response(data={'detail': 'Program Does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def get_queryset(self, program):
        orders = self.queryset.filter(program=program)
        return orders

    def list(self, request, *args, **kwargs):
        program = self.get_program(kwargs['program_id'])
        queryset = self.get_queryset(program)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProgramOrdersDetailView(APIView):
    permission_classes = (IsAuthenticated, IsOwner)

    def get_program(self, program_id):
        try:
            program = Program.objects.get(id=program_id)
            self.check_object_permissions(self.request, program)
            return program
        except Program.DoesNotExist:
            return Response(data={'detail': 'Program Does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def get_object(self, id):
        try:
            return Order.objects.get(id=id)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, program_id, pk, format=None):
        program = self.get_program(program_id)
        order = self.get_object(pk)
        if not order.program.id == program_id:
            return Response({'detail': 'Request Denied'}, status=status.HTTP_403_FORBIDDEN)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, program_id, pk, format=None):
        program = self.get_program(program_id)
        order = self.get_object(pk)
        if not order.program.id == program_id:
            return Response({'detail': 'Request Denied'}, status=status.HTTP_403_FORBIDDEN)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, program_id, pk, format=None):
        program = self.get_program(program_id)
        order = self.get_object(pk)
        if not order.program.id == program_id:
            return Response({'detail': 'Request Denied'}, status=status.HTTP_403_FORBIDDEN)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(('GET',))
def access_token(request, program_id):
    try:
        program = Program.objects.get(id=program_id)
        if request.user != program.owner:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={'detail': 'You are not authorized'})
        program.access_token = uuid.uuid4()
        program.save()
        return Response(status=status.HTTP_201_CREATED, data={'access_token': str(program.access_token)})
    except Program.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'detail': 'Program not found'})
