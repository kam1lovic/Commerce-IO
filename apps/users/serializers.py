from django.core.cache import cache
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer, CharField

from users.models import User
from users.tasks import send_welcome_email, generate_token


class SignUpSerializer(ModelSerializer):
    password = CharField(write_only=True)
    password2 = CharField(write_only=True)

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
        cache.set(f"user_id_by_token_{token}", user.id, time=60)

        send_welcome_email.delay(user.id, token)

        return user


class SignInSerializer(Serializer):
    email = serializers.EmailField(max_length=40, required=True)
    password = serializers.CharField(max_length=40, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')
