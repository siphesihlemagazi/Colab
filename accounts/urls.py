from django.urls import path
from accounts.views import (
    RegistrationAPIView,
    LoginAPIView,
    UserListAPIView,
    PasswordResetView,
    PasswordResetConfirm
)


app_name = "accounts"

urlpatterns = [
    path('register/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('users/', UserListAPIView.as_view()),
    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset-confirm/', PasswordResetConfirm.as_view())
]
