from rest_framework import serializers
from programs.models import Program
# from authentication.models import User


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ('id', 'name', 'incentive', 'access_token', 'is_active')
