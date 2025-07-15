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

    def validate(self, data):
        """Основная валидация в привычках"""
        validator = HabitValidator()
        return validator(data)

# [
#     {
#         "id": 1,
#         "place": "Прямо здесь",
#         "time": "2025-07-14T20:08:14+03:00",
#         "action": "Гулять",
#         "is_pleasant": true,
#         "periodicity": 1,
#         "reward": "Пирожок с полки",
#         "execution_time": 120,
#         "is_public": true,
#         "last_completed": null,
#         "user": 1,
#         "related_habit": null
#     }
# ]