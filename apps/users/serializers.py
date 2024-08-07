from users.models import User
from django.core.cache import cache
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from users.tasks import send_welcome_email, generate_token


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise ValidationError('Passwords do not match')
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)

        token = generate_token()
        cache.set(f"user_token_{user.id}", token, timeout=60)

        send_welcome_email.delay(user.id, token)

        return user

class UserLoginSerializer(Serializer):
    email = serializers.EmailField(max_length=40, required=True)
    password = serializers.CharField(max_length=40, required=True, write_only=True)
