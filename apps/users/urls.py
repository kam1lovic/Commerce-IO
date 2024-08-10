from django.urls import path

from users.views.users import UserCreateAPIView, UserLoginAPIView, ConfirmAccountView, LogoutAPIView

urlpatterns = [
    path('sign-up', UserCreateAPIView.as_view(), name='sign-up'),
    path('sign-in', UserLoginAPIView.as_view(), name='sign-in'),
    path('confirm/<str:token>', ConfirmAccountView.as_view(), name='confirm_account'),
    path('signout', LogoutAPIView.as_view(), name='logout')
]
