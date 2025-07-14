"""
Модели приложения `accounts`.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Пользователь"""

    username = models.CharField(
        max_length=50,
        verbose_name="Ник пользователя",
        null=True,
        blank=True,
        help_text="Укажите ник пользователя",
    )
    email = models.EmailField(
        unique=True, verbose_name="Почтовый адрес", help_text="Введите почтовый адрес"
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Укажите телефон",
    )
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
