from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import OrderSerializer, OrderDetailSerializer
from .permissions import IsOwner
from orders.models import Order
from programs.models import Program
from api.v1.exceptions import ProgramNotFound, ProgramIdNotFound


class OrderList(generics.ListAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Order.objects.all()

    def get_queryset(self):
        program_id = self.request.query_params.get('program_id')
        if not program_id:
            raise ProgramIdNotFound
        try:
            program = Program.objects.get(id=program_id)
            return program.program_orders.all()
        except Program.DoesNotExist:
            raise ProgramNotFound


class OrderCreate(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Order.objects.all()


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    queryset = Order.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = OrderDetailSerializer(instance)
        return Response(serializer.data)
