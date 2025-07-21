"""
Кастомные права доступа для приложения`habits`.
"""

from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверка прав для взаимодействия с приложением"""

    def has_object_permission(self, request, view, obj):
        """Проверка, является ли пользователь создателем привычки"""
        return bool(obj.user == request.user)
