"""
Представления приложения `habits`.
"""

from rest_framework import viewsets

from .models import Habit
from .serializers import HabitSerializer


class HabitModelViewSet(viewsets.ModelViewSet):
    """Генерация CRUD для модели `Habit`"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
