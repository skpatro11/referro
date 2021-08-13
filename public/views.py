from orders.serializers import OrderSerializer
from rest_framework import generics, serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from orders.models import Order
from orders.serializers import OrderSerializer
from members.models import Member
from members.serializers import MemberSerializer
from programs.models import Program
from programs.serializers import ProgramSerializer
from django.http import Http404


class ProgramListView(APIView):
    def valid_access_token(self, program, access_token):
        if not str(program.access_token) == access_token:
            return False
        return True

    def get(self, request, pk):
        try:
            program = Program.objects.get(pk=pk)
            access_token = request.META['HTTP_PROGRAM_ACCESS_TOKEN']
            if not self.valid_access_token(program, access_token):
                return Response({'detail': 'Invalid Access Token'}, status=status.HTTP_403_FORBIDDEN)
            serializer = ProgramSerializer(program)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Program.DoesNotExist:
            raise Http404


class MemberListView(generics.ListCreateAPIView):
    serializer_class = MemberSerializer

    def valid_access_token(self, program, access_token):
        if not str(program.access_token) == access_token:
            return False
        return True

    def get(self, request, pk):
        try:
            program = Program.objects.get(pk=pk)
            access_token = request.META['HTTP_PROGRAM_ACCESS_TOKEN']
            if not self.valid_access_token(program, access_token):
                return Response({'detail': 'Invalid Access Token'}, status=status.HTTP_403_FORBIDDEN)

            queryset = program.members.all()
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Program.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        try:
            program = Program.objects.get(pk=pk)
            access_token = request.META['HTTP_PROGRAM_ACCESS_TOKEN']
            if not self.valid_access_token(program, access_token):
                return Response({'detail': 'Invalid Access Token'}, status=status.HTTP_403_FORBIDDEN)

            serializer = MemberSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(program=program)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Program.DoesNotExist:
            raise Http404


class OrdersListView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def valid_access_token(self, program, access_token):
        if not str(program.access_token) == access_token:
            return False
        return True

    def get(self, request, pk):
        try:
            program = Program.objects.get(pk=pk)
            access_token = request.META['HTTP_PROGRAM_ACCESS_TOKEN']
            if not self.valid_access_token(program, access_token):
                return Response({'detail': 'Invalid Access Token'}, status=status.HTTP_403_FORBIDDEN)

            queryset = program.program_orders.all()
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Program.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        try:
            program = Program.objects.get(pk=pk)
            access_token = request.META['HTTP_PROGRAM_ACCESS_TOKEN']
            if not self.valid_access_token(program, access_token):
                return Response({'detail': 'Invalid Access Token'}, status=status.HTTP_403_FORBIDDEN)

            try:
                member = Member.objects.get(id=request.data['member'])
                if not member.program.id == pk:
                    return Response(data={'detail': 'Request Denied'}, status=status.HTTP_403_FORBIDDEN)
                request.data['claim_amount'] = float(program.incentive)
                request.data['charge_amount'] = float(program.incentive) + 0.05 * float(program.incentive)
            except Member.DoesNotExist:
                raise Http404

            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(program=program)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Program.DoesNotExist:
            raise Http404


class MemberDetailView(APIView):
    def valid_access_token(self, program, access_token):
        if not str(program.access_token) == access_token:
            return False
        return True

    def get(self, request, program_id, pk):
        try:
            program = Program.objects.get(pk=program_id)
            access_token = request.META['HTTP_PROGRAM_ACCESS_TOKEN']
            if not self.valid_access_token(program, access_token):
                return Response({'detail': 'Invalid Access Token'}, status=status.HTTP_403_FORBIDDEN)

            try:
                member = Member.objects.get(pk=pk)
                if not member.program.id == program_id:
                    return Response({'detail': 'Invalid Access'}, status=status.HTTP_403_FORBIDDEN)
                serializer = MemberSerializer(member)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Member.DoesNotExist:
                raise Http404
        except Program.DoesNotExist:
            raise Http404

    def put(self, request, program_id, pk):
        try:
            program = Program.objects.get(pk=program_id)
            access_token = request.META['HTTP_PROGRAM_ACCESS_TOKEN']
            if not self.valid_access_token(program, access_token):
                return Response({'detail': 'Invalid Access Token'}, status=status.HTTP_403_FORBIDDEN)

            try:
                member = Member.objects.get(pk=pk)
                if not member.program.id == program_id:
                    return Response({'detail': 'Invalid Access'}, status=status.HTTP_403_FORBIDDEN)
                serializer = MemberSerializer(member, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Member.DoesNotExist:
                raise Http404
        except Program.DoesNotExist:
            raise Http404

    def delete(self, request, program_id, pk):
        try:
            program = Program.objects.get(pk=program_id)
            access_token = request.META['HTTP_PROGRAM_ACCESS_TOKEN']
            if not self.valid_access_token(program, access_token):
                return Response({'detail': 'Invalid Access Token'}, status=status.HTTP_403_FORBIDDEN)

            try:
                member = Member.objects.get(pk=pk)
                if not member.program.id == program_id:
                    return Response({'detail': 'Invalid Access'}, status=status.HTTP_403_FORBIDDEN)

                member.delete()
                return Response(data={'detail': 'Member deleted'})
            except Member.DoesNotExist:
                raise Http404
        except Program.DoesNotExist:
            raise Http404


class OrderDetailView(APIView):
    def valid_access_token(self, program, access_token):
        if not str(program.access_token) == access_token:
            return False
        return True

    def get(self, request, program_id, pk):
        try:
            program = Program.objects.get(pk=program_id)
            access_token = request.META['HTTP_PROGRAM_ACCESS_TOKEN']
            if not self.valid_access_token(program, access_token):
                return Response({'detail': 'Invalid Access Token'}, status=status.HTTP_403_FORBIDDEN)

            try:
                order = Order.objects.get(pk=pk)
                if not order.program.id == program_id:
                    return Response({'detail': 'Invalid Access'}, status=status.HTTP_403_FORBIDDEN)
                serializer = OrderSerializer(order)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Order.DoesNotExist:
                raise Http404
        except Order.DoesNotExist:
            raise Http404

    def put(self, request, program_id, pk):
        try:
            program = Program.objects.get(pk=program_id)
            access_token = request.META['HTTP_PROGRAM_ACCESS_TOKEN']
            if not self.valid_access_token(program, access_token):
                return Response({'detail': 'Invalid Access Token'}, status=status.HTTP_403_FORBIDDEN)

            try:
                order = Order.objects.get(pk=pk)
                if not order.program.id == program_id:
                    return Response({'detail': 'Invalid Access'}, status=status.HTTP_403_FORBIDDEN)
                serializer = OrderSerializer(order, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Order.DoesNotExist:
                raise Http404
        except Program.DoesNotExist:
            raise Http404

    def delete(self, request, program_id, pk):
        try:
            program = Program.objects.get(pk=program_id)
            access_token = request.META['HTTP_PROGRAM_ACCESS_TOKEN']
            if not self.valid_access_token(program, access_token):
                return Response({'detail': 'Invalid Access Token'}, status=status.HTTP_403_FORBIDDEN)

            try:
                order = Order.objects.get(pk=pk)
                if not order.program.id == program_id:
                    return Response({'detail': 'Invalid Access'}, status=status.HTTP_403_FORBIDDEN)

                order.delete()
                return Response(data={'detail': 'Member deleted'})
            except Order.DoesNotExist:
                raise Http404
        except Program.DoesNotExist:
            raise Http404
