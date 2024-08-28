from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from rest_framework import serializers
from rest_framework.serializers import CharField, ModelSerializer, Serializer

from root import settings
from users.models.users import User


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
        user.save()

        token = default_token_generator.make_token(user)
        cache.set(f'email_confirm_token_{token}', user.pk, timout=60)

        request = self.context['request']
        protocol = 'https' if request.is_secure() else 'http'
        domain = get_current_site(request).domain
        link = reverse('confirm_account', kwargs={'token': token})
        activate_url = f'{protocol}://{domain}{link}'

        email_subject = 'Activate your account'
        email_body = render_to_string('users/welcome_email.html', {
            'user': user,
            'activate_url': activate_url
        })

        send_mail(
            email_subject,
            '',
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
            html_message=email_body
        )

        return user


class SignInSerializer(Serializer):
    email = serializers.EmailField(max_length=40, required=True)
    password = serializers.CharField(max_length=40, required=True, write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not email or not password:
            raise ValidationError('Email and password are required.')

        user = authenticate(username=email, password=password)
        if user is None or not user.is_active:
            raise ValidationError('Invalid email or password.')

        attrs['user'] = user
        return attrs
