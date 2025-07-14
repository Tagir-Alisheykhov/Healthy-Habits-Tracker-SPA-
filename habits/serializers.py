"""
Сериализация моделей приложения `habits`.
"""

from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """Сериализация модели Привычка"""

    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self):
        """Основная валидация в привычках"""

