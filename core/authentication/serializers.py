from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.serializers import PasswordField
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    password = PasswordField(required=True)
    password2 = PasswordField(required=True)
    username = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = User
        fields = ['password', 'password2', 'username']


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        from rest_framework_simplejwt.tokens import RefreshToken
        ret['token'] = {
            'refresh': f'{RefreshToken.for_user(instance)}',
            'access_token': f'{RefreshToken.for_user(instance).access_token}'
        }
        return ret

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = PasswordField(required=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name']

    def create(self, validated_data):
        user: User = authenticate(**validated_data)
        if not user or not user.is_active:
            raise AuthenticationFailed('Username or password is incorrect.')
        return user

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        from rest_framework_simplejwt.tokens import RefreshToken
        ret['token'] = {
            'refresh': f'{RefreshToken.for_user(instance)}',
            'access_token': f'{RefreshToken.for_user(instance).access_token}'
        }
        return ret
