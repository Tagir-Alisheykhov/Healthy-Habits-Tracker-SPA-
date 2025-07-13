"""
Файл для распаковки конфигурационных данных из переменных окружения.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class ShadowKeys:
    """Получение переменных окружения по ключам."""

    DEBUG = True if os.getenv("DEBUG") == "True" else False
    SECRET_KEYS = os.getenv("SECRET_KEY")

