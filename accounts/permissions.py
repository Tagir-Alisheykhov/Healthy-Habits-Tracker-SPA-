"""
Кастомные классы прав доступа, для приложения `accounts`.
"""

from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверяет, является ли пользователь создателем/владельцем объекта"""

    def has_object_permission(self, request, view, obj) -> bool:
        """Проверка, является ли пользователь владельцем аккаунта"""
        return bool(obj.email == request.user.email)
