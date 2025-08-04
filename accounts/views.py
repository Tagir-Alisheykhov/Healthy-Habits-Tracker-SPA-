"""
Отображение моделей приложения `accounts`.
"""

from rest_framework import viewsets
from rest_framework.permissions import (AND, OR, AllowAny, IsAdminUser,
                                        IsAuthenticated)

from accounts.models import User
from accounts.permissions import IsOwner
from accounts.serializers import UserSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    """CRUD для модели `User`"""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """Разные права для разных действий"""
        if self.action == "create":
            return [AllowAny()]
        elif self.action in ["retrieve", "update", "partial_update"]:
            return [OR(AND(IsAuthenticated(), IsOwner()), IsAdminUser())]
        return [IsAdminUser()]

    def get_object(self):
        """Получение информации о текущем пользователе"""
        if self.request.path.endswith("/me/"):
            return self.request.user
        return super().get_object()
