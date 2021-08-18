from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import OrderSerializer, OrderDetailSerializer
from orders.models import Order
from programs.models import Program


class OrderList(generics.ListAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Order.objects.all()

    def get_queryset(self):
        programs = self.request.user.programs.all()
        queryset = None
        for program in programs:
            if queryset is None:
                queryset = program.program_orders.all()
            else:
                queryset = queryset.union(program.program_orders.all())
        return queryset


class OrderCreate(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Order.objects.all()


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Order.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = OrderDetailSerializer(instance)
        return Response(serializer.data)
