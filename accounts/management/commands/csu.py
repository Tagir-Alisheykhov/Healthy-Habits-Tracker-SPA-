"""
Создание суперпользователя.
[>> python manage.py csu ]
"""

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from config.shadow import ShadowKeys

shadow = ShadowKeys()

FIRSTNAME = shadow.SUPERUSER_FIRST_NAME
LASTNAME = shadow.SUPERUSER_LAST_NAME
PASSWORD = shadow.SUPERUSER_PASSWORD
EMAIL = shadow.SUPERUSER_EMAIL


class Command(BaseCommand):
    """Команда для создания суперпользователя"""

    def handle(self, *args, **options):
        us_model = get_user_model()
        user = us_model.objects.create(
            email=EMAIL, first_name=FIRSTNAME, last_name=LASTNAME
        )
        user.set_password(PASSWORD)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created superuser with email `{user.email}`!"
            )
        )
