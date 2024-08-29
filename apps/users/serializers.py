from rest_framework import serializers

from django.contrib.auth.models import User


def validate_username(attrs):
    if 'admin' in attrs:
        raise serializers.ValidationError('admin is not non !!!')
    return attrs


def validate_email(attrs):
    if '@gmail.com' in attrs:
        return attrs
    else:
        raise serializers.ValidationError('is not a valid email !!!')


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'username': {
                'validators': [validate_username]
            },
            'email': {
                'validators': [validate_email]
            }
        }


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
