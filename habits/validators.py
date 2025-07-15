"""
Валидаторы приложения `habits`.
"""

from rest_framework import serializers


class HabitValidator:
    """Валидация объекта модели Habit"""

    def __call__(self, data):
        """Основная валидация привычек"""
        related_habit = data.get("related_habit")
        reward = data.get("reward")
        is_pleasant = data.get("is_pleasant")
        periodicity = data.get("periodicity", 1)

        if related_habit and reward:
            raise serializers.ValidationError(
                "Нельзя указывать и связанную привычку, и вознаграждение одновременно."
            )
        if is_pleasant is True and (reward or related_habit):
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки."
            )
        if periodicity > 7:
            raise serializers.ValidationError(
                "Нельзя не выполнять привычку более 7 дней."
            )
        if related_habit and not related_habit.is_pleasant:
            raise serializers.ValidationError(
                "Связанная привычка должна быть приятной."
            )
        return data
