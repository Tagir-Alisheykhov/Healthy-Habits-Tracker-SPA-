"""
Конфигурационные настройки Django-проекта.
"""

import os
from datetime import timedelta
from pathlib import Path

from config.shadow import ShadowKeys

shadow = ShadowKeys()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = shadow.SECRET_KEY

DEBUG = shadow.DEBUG

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "rest_framework_simplejwt",
    "django_celery_beat",
    "rest_framework",
    "django_filters",
    "corsheaders",
    "accounts",
    "drf_yasg",
    "habits",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]


ROOT_URLCONF = "config.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=1440),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": shadow.DB_NAME,
        "USER": shadow.DB_USER,
        "PASSWORD": shadow.DB_PASSWORD,
        "HOST": shadow.DB_HOST,
        "PORT": shadow.DB_PORT,
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

AUTH_USER_MODEL = "accounts.User"


# Настройка для celery
# URL-адрес брокера сообщений
CELERY_BROKER_URL = shadow.CELERY_URL
# URL-адрес брокера результатов, также Redis
CELERY_RESULT_BACKEND = shadow.CELERY_URL
# Часовой пояс для работы Celery
CELERY_TIMEZONE = "Europe/Moscow"
# Флаг отслеживания выполнения задач
# CELERY_TASK_TRACK_STARTED = True
# Максимальное время на выполнение задачи
# CELERY_TASK_TIME_LIMIT = 30 * 60

# celery-beat настройка
CELERY_BEAT_SCHEDULE = {
    "deactivate-inactive-users": {
        "task": "habits.tasks.check_and_send_habit_reminders",
        "schedule": timedelta(minutes=15),
    },
}

# Настройка Redis
CACHE_ENABLED = shadow.REDIS_CACHE_ENABLED
if CACHE_ENABLED:
    CACHES = {
        "default": {
            "BACKEND": shadow.REDIS_BACKEND,
            "LOCATION": shadow.REDIS_LOCATION,
        }
    }

# Настройка отправки уведомлений на почту.
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = shadow.EMAIL_HOST
EMAIL_PORT = shadow.EMAIL_PORT
EMAIL_USE_TLS = shadow.EMAIL_USE_TLS
EMAIL_USE_SSL = shadow.EMAIL_USE_SSL
EMAIL_HOST_USER = shadow.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = shadow.EMAIL_HOST_PASSWORD
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER


# Настойка CORS
CORS_ALLOWED_ORIGINS = [shadow.CORS_FRONTEND]
CSRF_TRUSTED_ORIGINS = [
    shadow.CORS_FRONTEND,
    # shadow.CORS_BACKEND # Если разные домены
]
CORS_ALLOW_ALL_ORIGINS = shadow.CORS_ALLOW_ALL_ORIGINS
# CORS_ALLOW_CREDENTIALS = True  # Если фронтенд отправляет куки
