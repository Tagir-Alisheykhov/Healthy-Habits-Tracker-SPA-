"""
Отображение моделей приложения `accounts`.
"""

from rest_framework import viewsets

from .serializers import UserSerializer
from .models import User


class UserModelViewSet(viewsets.ModelViewSet):
    """CRUD для модели `User`"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
