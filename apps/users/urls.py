from django.urls import path

from users.views import UserCreateAPIView, UserLoginAPIView, ConfirmAccountView

urlpatterns = [
    path('sign-up', UserCreateAPIView.as_view(), name='sign-up'),
    path('sign-in', UserLoginAPIView.as_view(), name='sign-in'),
    path('confirm/<int:user_id>/<str:token>', ConfirmAccountView.as_view(), name='confirm_account'),

]
