
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,  max_length=8)


    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            password= validated_data['password'],
            email= validated_data['email']
        )
        return user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True,  max_length=8)

    def validate(self, data):
        username = data.get['username']
        password = data.get['password']

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("invalid username or password")

        refresh = RefreshToken.for_user(user)
        return {
            "refresh": refresh,
            "access": refresh.access_token
        }










