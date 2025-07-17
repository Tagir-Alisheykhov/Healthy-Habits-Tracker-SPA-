"""
Представления приложения `habits`.
"""

from django.db.models import Q
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AND, IsAuthenticated, IsAdminUser

from habits.models import Habit
from habits.paginators import HabitsPagination
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitModelViewSet(viewsets.ModelViewSet):
    """
    Генерация CRUD для модели `Habit`.
    Параметры:
    - ?is_public=true — только публичные привычки
    - ?search=текст — поиск по action, place, reward
    - ?ordering=поле — сортировка
    """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitsPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["action", "place", "reward"]
    ordering = ["time"]

    def perform_create(self, serializer):
        """Автоматическое назначение текущего пользователя"""
        user = self.request.user
        serializer.save(user=user)

    def get_queryset(self):
        """
        Фильтр привычек:
        - Для админов: все привычки
        - Для обычных пользователей: свои + публичные
        - При ?is_public=true: только публичные (общедоступные)
        """
        queryset = super().get_queryset()
        if self.request.query_params.get("is_public") == "true":
            return queryset.filter(is_public=True)
        if self.request.user.is_superuser:
            return self.queryset
        return queryset.filter(Q(user=self.request.user) | Q(is_public=True))

    def get_permissions(self):
        """Разные права под разные действия"""
        if self.action == "create":
            return [IsAuthenticated()]
        elif self.action in ("list", "retrieve"):
            return [IsAuthenticated()]
        elif self.action in ("update", "partial_update", "destroy"):
            return [AND(IsOwner(), IsAuthenticated())]
        return [IsAdminUser()]
