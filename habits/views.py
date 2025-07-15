"""
Представления приложения `habits`.
"""

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Habit
from .paginators import HabitsPagination
from .serializers import HabitSerializer


class HabitModelViewSet(viewsets.ModelViewSet):
    """Генерация CRUD для модели `Habit`"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitsPagination

    def perform_create(self, serializer):
        """Автоматическое назначение пользователя при создании"""
        serializer.save(user=self.request.user)

    @action(detail=False, methods=["get"])
    def public(self, request):
        """
        Конечная точка, для вывода списка публичных привычек
        для вывода данных, добавьте /public/ к пути текущего приложения.
        """
        queryset = Habit.objects.filter(is_public=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
