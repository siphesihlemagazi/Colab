from accounts.serializers import RegistrationSerializer, LoginSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode
from rest_framework import response, status, permissions, serializers
from rest_framework.generics import GenericAPIView
from accounts.models import User
from accounts.serializers import PasswordResetSerializer, PasswordResetConfirmSerializer

from colab_api.settings import EMAIL_HOST_USER
from django.utils.http import urlsafe_base64_decode


class UserListAPIView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = RegistrationSerializer(user)
        return response.Response({'user': serializer.data})


class RegistrationAPIView(GenericAPIView):
    authentication_classes = []

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,
                                     status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors,
                                 status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    # Update this to use the new jwt implementation
    authentication_classes = []
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)

        if user and user.is_active:
            serializer = self.serializer_class(user)

            # Create cookie
            # response.Response().set_cookie(key='jwt', value=serializer.data['token'], httponly=False)
            return response.Response(serializer.data, status=status.HTTP_200_OK)

        return response.Response(
            {'message': "Invalid credentials, try again."},
            status=status.HTTP_401_UNAUTHORIZED
        )


class PasswordResetView(GenericAPIView):
    """
    Takes a password_reset_confirm_url parameter to build url to send a user to the client's
    password reset confirm page.
    """
    authentication_classes = []
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password_reset_confirm_fullpath = serializer.validated_data['password_reset_confirm_fullpath']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return response.Response({"message": "Email not found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = f"{password_reset_confirm_fullpath}?uid={uid}&token={token}"
            send_mail(
                'Password reset request',
                f'Use the following link to reset your password: {reset_link}',
                EMAIL_HOST_USER,
                [user.email],
                fail_silently=False
            )
            return response.Response({"message": "Password reset email sent"})


class PasswordResetConfirm(GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user = User.objects.get(pk=force_str(urlsafe_base64_decode(serializer.validated_data['uid'])))
            user.set_password(serializer.validated_data['password'])
            user.save()
            return response.Response({"message": "Password updated successfully"})
        except serializers.ValidationError as e:
            print("Error", e.details)
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
