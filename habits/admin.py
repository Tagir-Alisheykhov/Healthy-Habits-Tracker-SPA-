from django.contrib import admin

from .models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """Отображение модели привычки в админ-панели"""

    list_display = (
        "user",
        "place",
        "time",
        "action",
        "is_pleasant",
        "related_habit",
        "reward",
        "execution_time",
        "is_public",
        "last_completed",
    )
    list_filter = (
        "time",
        "user",
    )
    search_fields = ("user", "time", "is_public", "reward")
