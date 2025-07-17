"""
Сериализация моделей приложения `accounts`.
"""
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализация модели Пользователя"""

    class Meta:
        model = User
        fields = ["id", "email", "password", "first_name", "last_name"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """Хэш паролей перед созданием"""
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
