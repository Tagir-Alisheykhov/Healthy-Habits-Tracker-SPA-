"""
Файл для распаковки конфигурационных данных из переменных окружения.
"""

import os

from dotenv import load_dotenv

load_dotenv()


class ShadowKeys:
    """Получение переменных окружения по ключам."""

    # basic settings
    DEBUG = True if os.getenv("DEBUG") == "True" else False
    SECRET_KEY = os.getenv("SECRET_KEY")

    # create superuser
    SUPERUSER_FIRST_NAME = os.getenv("SUPERUSER_FIRST_NAME")
    SUPERUSER_LAST_NAME = os.getenv("SUPERUSER_LAST_NAME")
    SUPERUSER_PASSWORD = os.getenv("SUPERUSER_PASSWORD")
    SUPERUSER_EMAIL = os.getenv("SUPERUSER_EMAIL")

    # Настройка для redis
    REDIS_CACHE_ENABLED = os.getenv("REDIS_CACHE_ENABLED")
    REDIS_LOCATION = os.getenv("REDIS_LOCATION")
    REDIS_BACKEND = os.getenv("REDIS_BACKEND")

    # Email backend
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
    EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
    EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")
    EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL")
    EMAIL_HOST = os.getenv("EMAIL_HOST")
    EMAIL_PORT = os.getenv("EMAIL_PORT")

    # Настройка для celery
    CELERY_URL = os.getenv("CELERY_URL")

    # database
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")


