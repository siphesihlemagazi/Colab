from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers
from accounts.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']

        read_only_fields = ['token']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password_reset_confirm_fullpath = serializers.CharField(required=True, max_length=128)


class PasswordResetConfirmSerializer(serializers.Serializer):
    password = serializers.CharField(required=True, max_length=128)
    password2 = serializers.CharField(required=True, max_length=128)
    uid = serializers.CharField(required=True, max_length=128)
    token = serializers.CharField(required=True, max_length=128)

    def validate(self, data):
        uid = force_str(urlsafe_base64_decode(data['uid']))
        user = User.objects.get(pk=uid)
        if not user:
            print(f'Error: user with id {uid} does not exist')
            raise serializers.ValidationError({'user': 'This user does not exist.'})

        if not default_token_generator.check_token(user, data['token']):
            print('Error: Token is invalid')
            raise serializers.ValidationError({
                'link': 'This link is not valid, make new password reset request.'
            })

        if data['password'] != data['password2']:
            raise serializers.ValidationError({'passwords': 'Passwords do not match.'})

        try:
            validate_password(data['password'])
        except Exception as e:
            raise serializers.ValidationError({'passwords': str(e)})

        return data

