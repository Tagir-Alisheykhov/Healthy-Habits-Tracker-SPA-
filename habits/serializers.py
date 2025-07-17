"""
Сериализация моделей приложения `habits`.
"""

from rest_framework import serializers

from habits.models import Habit
from habits.validators import HabitValidator


class HabitSerializer(serializers.ModelSerializer):
    """Сериализация модели Привычка"""

    class Meta:
        model = Habit
        fields = "__all__"
        read_only_fields = ("user",)

    def validate(self, data):
        """Основная валидация в привычках"""
        validator = HabitValidator()
        return validator(data)
