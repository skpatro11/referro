from rest_framework import serializers
from orders.models import Order
from members.models import Member
from programs.models import Program

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ('id', 'name', 'incentive')

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'username', 'created_at')

class OrderDetailSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)
    program = ProgramSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'member', 'program', 'claim_amount', 'charge_amount', 'status', 'created_at')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'member', 'program', 'claim_amount', 'charge_amount', 'status', 'created_at')
