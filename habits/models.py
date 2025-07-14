"""
Модели приложения `habits`.
"""
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from accounts.models import User


class Habit(models.Model):
    """Модель для создания полезной привычки"""

    PERIODICITY_CHOICES = [
        (1, "Ежедневно"),
        (2, "Через день"),
        (3, "Еженедельно"),
        (7, "Раз в неделю"),
    ]
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="habits"
    )
    place = models.CharField(
        max_length=255,
        verbose_name="Место выполнения"
    )
    time = models.DateTimeField(
        verbose_name="Дата и время выполнения"
    )
    action = models.CharField(
        max_length=255,
        verbose_name="Действие"
    )
    is_pleasant = models.BooleanField(
        default=False,
        verbose_name="Приятная привычка"
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Связанная привычка",
    )
    periodicity = models.PositiveSmallIntegerField(
        choices=PERIODICITY_CHOICES,
        default=1,
        verbose_name="Периодичность (дни)",
        validators=[MinValueValidator(1), MaxValueValidator(7)]
    )
    reward = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Вознаграждение"
    )
    execution_time = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(120)],
        verbose_name="Время на выполнение (секунды)"
    )
    is_public = models.BooleanField(
        default=False,
        verbose_name="Публичная привычка"
    )
    last_completed = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Последнее выполнение"
    )

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
