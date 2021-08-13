from rest_framework import serializers
from .models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'is_active', 'verify_counter', 'is_admin',
                   'is_email_verified', 'is_phone_verified', 'roles')


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'phone')

    def create(self, validated_data):
        user = User.objects.create(name=validated_data['name'],
                                   email=validated_data['email'], phone=validated_data['phone'])

        user.set_password(validated_data['password'])
        user.save()

        return user
