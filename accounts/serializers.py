"""
Сериализация моделей приложения `accounts`.
"""

from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализация модели Пользователя"""

    class Meta:
        model = User
        fields = "__all__"
