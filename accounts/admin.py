"""
Настройки отображения объектов моделей в админ-панели django
"""

from django.contrib import admin

from accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Отображение модели пользователя"""

    list_display = (
        "email",
        "phone",
        "avatar",
    )
    list_filter = ("email", "phone")
    search_fields = (
        "email",
        "phone",
    )
