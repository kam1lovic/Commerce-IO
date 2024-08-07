from django.contrib.auth import authenticate
from django.core.cache import cache
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import SignUpSerializer, UserLoginSerializer
from users.tasks import generate_unique_invitation_code


@extend_schema(tags=['Authorizations'])
class UserCreateAPIView(CreateAPIView):
    model = User
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer


@extend_schema(tags=['Authorizations'])
class ConfirmAccountView(APIView):
    permission_classes = [AllowAny]


    def get(self, request, user_id, token):
        cached_token = cache.get(f"user_token_{user_id}")
        if cached_token == token:
            try:
                user = User.objects.get(pk=user_id)
                user.public_offer = True
                user.is_active = True
                user.invitation_code = generate_unique_invitation_code()
                user.save()
                return Response({"detail": "Account confirmed successfully."}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"detail": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"detail": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['Authorizations'])
class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if user := authenticate(email=serializer.validated_data['email'],
                                password=serializer._validated_data['password'], is_active=True):
            token, created = Token.objects.get_or_create(user=user)
            response = {
                'token': token.key
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
