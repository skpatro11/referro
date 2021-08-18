from rest_framework import serializers
from members.models import Member
from programs.models import Program

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ('id', 'name')

class MemberProgramSerializer(serializers.ModelSerializer):
    program = ProgramSerializer(read_only=True)

    class Meta:
        model = Member
        fields = ('id', 'program', 'username', 'created_at')

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'program', 'username', 'created_at')
