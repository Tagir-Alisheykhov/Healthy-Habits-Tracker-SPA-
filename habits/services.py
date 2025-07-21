"""
Сервисные функции приложения `habits`.
"""

import requests
from config.shadow import ShadowKeys

shadow = ShadowKeys()


def send_telegram_message(chat_id: int, message: str) -> None:
    """
    Отправка уведомлений пользователю в телеграм.
    - chat_id: пользователя в телеграм.
    - message: содержит текст сообщения.
    """
    url = f"{shadow.TG_BASE_URL}{shadow.TG_BOT_HTTP_TOKEN}/sendMessage"
    params = {"text": message, "chat_id": chat_id}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        json_data = response.json()
        print("Ответ API:", json_data)
    else:
        print(f"Ошибка: {response.status_code}")
