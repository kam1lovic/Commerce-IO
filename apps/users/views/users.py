from django.contrib.auth import authenticate
from django.core.cache import cache
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers.users import (
    SignInSerializer,
    SignUpSerializer,
)
from users.tasks import generate_unique_invitation_code


@extend_schema(tags=['Authorizations'])
class UserCreateAPIView(CreateAPIView):
    model = User
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer


@extend_schema(tags=['Authorizations'])
class ConfirmAccountView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, token):
        user_id = cache.get(f"user_id_by_token_{token}")
        if user_id:
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
class UserLoginAPIView(GenericAPIView):
    serializer_class = SignInSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = SignInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if user := authenticate(email=serializer.validated_data['email'],
                                password=serializer._validated_data['password'], is_active=True):
            token, created = Token.objects.get_or_create(user=user)
            response = {
                'token': token.key
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['Authorizations'])
class LogoutAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()
        except (AttributeError, Token.DoesNotExist):
            return Response({"detail": "Token not found."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
