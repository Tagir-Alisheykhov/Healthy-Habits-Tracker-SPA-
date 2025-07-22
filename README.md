# Трекер полезных привычек
>В 2018 году Джеймс Клир написал книгу «Атомные привычки», 
которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек.
Данное приложение работает по основным принципам данной книги.

[![Django](https://img.shields.io/badge/Django-3.2.18-blue?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django REST](https://img.shields.io/badge/DRF-3.16.0-red?logo=json&logoColor=white)](https://www.django-rest-framework.org/)
[![Django Filter](https://img.shields.io/badge/django--filter-23.1-blue?logo=filter&logoColor=white)](https://django-filter.readthedocs.io/en/stable/)
[![SimpleJWT](https://img.shields.io/badge/Simple_JWT-5.2.2-ff69b4?logo=jsonwebtokens&logoColor=white)](https://django-rest-framework-simplejwt.readthedocs.io/)
[![Python](https://img.shields.io/badge/Python-3.11+-yellow?logo=python&logoColor=white)](https://www.python.org/)
[![drf-yasg](https://img.shields.io/badge/drf--yasg-1.21.6-brightgreen?logo=swagger&logoColor=white)](https://drf-yasg.readthedocs.io/en/stable/readme.html#usage)
[![django-cors-headers](https://img.shields.io/badge/django--cors--headers-4.3.1-success?logo=cors&logoColor=white)](https://pypi.org/project/django-cors-headers/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)
[![Redis](https://img.shields.io/badge/Redis-7.0+-red?logo=redis&logoColor=white)](https://redis.readthedocs.io/en/stable/index.html)
[![Celery](https://img.shields.io/badge/Celery-5.3+-informational?logo=celery&logoColor=white)](https://docs.celeryq.dev/en/stable/)
[![Celery Beat](https://img.shields.io/badge/Celery_Beat-2.5.0-blueviolet?logo=clockify&logoColor=white)](https://pypi.org/project/django-celery-beat/)
[![Telegram API Docs](https://img.shields.io/badge/Telegram_API_Documentation-6.9-2CA5E0?logo=telegram&logoColor=white)](https://core.telegram.org/api)
[![Docker](https://img.shields.io/badge/Docker-24.0+-blue?logo=docker&logoColor=white)](https://docs.docker.com/)
[![Docker Compose](https://img.shields.io/badge/Docker_Compose-2.23+-blue?logo=docker&logoColor=white)](https://docs.docker.com/compose/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-blue?logo=postgresql&logoColor=white)](https://hub.docker.com/_/postgres)

---

## 🧰 _Настройка проекта_

### 1. Клонируйте репозиторий
```commandline
git clone git@github.com:Tagir-Alisheykhov/Healthy-Habits-Tracker-SPA-.git
``` 
```commandline
cd Healthy-Habits-Tracker-SPA  
```

### 2. Заполнение переменных окружения `.env` 
> Скопируйте шаблонный файл (`.env.example`) в корневой директории проекта и создайте 
> `.env` (без `.example`), заполнив 
> конфигурационные поля реальными данными. Программа автоматически 
> загрузит эти данные для работы приложения. 


## 🚀 Запуск проекта с Docker Compose

### 1. Сборка и запуск контейнеров

Перед запуском программы необходимо убедиться, что у вас на ПК установлен `Docker`.  
Выполните команду в корне проекта (где находится `docker-compose.yml`):

```bash
docker-compose up -d --build
```

## 📚 _Документация API_

Проект включает автоматически генерируемую документацию API с использованием Swagger и ReDoc:

>- **Swagger UI** - интерактивная документация с возможностью тестирования API:  
  [http://127.0.0.1:8000/swagger/](http://localhost:8000/swagger/)
  
>- **ReDoc** - альтернативное представление документации:  
  [http://127.0.0.1:8000/redoc/](http://localhost:8000/redoc/)

### Документация включает:
- Все доступные эндпоинты API
- Параметры запросов и ответов
- Примеры запросов
- Авторизацию через JWT

---

## 🌟 _Основные возможности_
- Управление привычками
- Создание, редактирование, просмотр привычек
- Публикация и снятие с публикации привычек
- Аутентификация и авторизация
- JWT-аутентификация
- Разграничение прав доступа
- Регистрация новых пользователей

---

## 🛠 _Технологический стек_
### Основной стек
- `Django 3.2` + `DRF 3.16` - backend
- `PostgreSQL 15` - основная БД
- `Redis` - кеш и брокер для Celery

### Инфраструктура
- `Docker` + `Docker Compose` - контейнеризация
- `Celery` + `Celery Beat` - асинхронные задачи

### Дополнительно
- `JWT` (`SimpleJWT`) - аутентификация
- `drf-yasg` - документация API
- `Telegram Bot API` - нотификации

---

## 📄 _Лицензия_
- MIT License © 2025
