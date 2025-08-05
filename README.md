<!DOCTYPE html>
<html>
<head>
<style>
  .habit-tracker-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 30px 20px;
    text-align: center;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    margin: 20px auto;
    max-width: 900px;
  }
  .habit-tracker-header h1 {
    font-family: 'Arial', sans-serif;
    font-size: 2.2em;
    margin-bottom: 15px;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
  }
  .habit-tracker-header .subtitle {
    font-family: 'Georgia', serif;
    font-style: italic;
    font-size: 1.1em;
    margin-bottom: 15px;
  }
  .habit-tracker-header p {
    font-family: 'Helvetica', sans-serif;
    font-size: 1em;
    line-height: 1.5;
  }
</style>
</head>
<body>

<div class="habit-tracker-header">
  <h1>ТРЕКЕР ПОЛЕЗНЫХ ПРИВЫЧЕК</h1>
  <div class="subtitle">Вдохновлено книгой «Атомные привычки» Джеймса Клира</div>
  <p>В 2018 году Джеймс Клир написал книгу «Атомные привычки», 
  которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек.
  Данное приложение работает по основным принципам данной книги.</p>
</div>

</body>
</html>

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
## ▶️ Ссылка на сервис
<a href="http://89.169.187.28/health/" style="display: inline-block; padding: 10px 20px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px; border: none; cursor: pointer;">Перейти к сервису</a>

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


## 🚀 Запуск проекта

### Вариант 1: Сборка и запуск контейнеров с Docker Compose

Перед запуском программы необходимо убедиться, что у вас на ПК установлен `Docker`.  
Выполните команду в корне проекта (где находится `docker-compose.yml`):

```bash
docker compose up -d --build
```
Выполнение миграций базы данных
```bash
docker compose exec backend python manage.py migrate
```
Сборка статических файлов
```bash
docker-compose exec backend python manage.py collectstatic --noinput
```
Создание суперпользователя (опционально)
```bash
docker-compose exec backend python manage.py csu
```
> Обратите внимание! Для локальной сборки, некоторые конфигурационные данные 
> автоматически переопределяются в `docker-compose.override.yml`. При автодеплое файл `docker-compose.override.yml` удаляется.   

### Вариант 2: Запуск локально (для разработки)
Активируйте виртуальное окружение Poetry
```bash
poetry shell
```
Запустите сервер разработки Django
```bash
python manage.py runserver
```

## 📚 _Документация API_

Проект включает автоматически генерируемую документацию API с использованием Swagger и ReDoc:

>- **Swagger UI** - интерактивная документация с возможностью тестирования API:  
  [http://89.169.187.28/swagger/](http://89.169.187.28/swagger/)
  
>- **ReDoc** - альтернативное представление документации:  
  [http://89.169.187.28/redoc/](http://89.169.187.28/redoc/)

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

## 🗄️ Структура проекта
- `healthy-habits-tracker/`
- ├── `.github/`           # Настройка CI/CD  
- ├── `accounts/`          # Приложение для управления пользователями
- ├── `habits/`            # Приложение для управления привычками
- ├── `config/ `           # Настройки проекта (settings, urls, wsgi)
- ├── `static/  `          # Статические файлы
- ├── `templates/`         # Шаблоны (если используются)
- ├── `manage.py  `        # Скрипт управления Django
- ├──` Dockerfile  `       # Конфигурация Docker для приложения
- ├── `docker-compose.yml` # Конфигурация Docker Compose
- ├── `docker-compose.override.yml` # Переопределение конфигурации для локальной сборки 
- ├── `nginx.conf         `# Конфигурация Nginx
- ├── `.env.sample        `# Шаблон файла переменных окружения
- ├── `pyproject.toml     `# Конфигурация Poetry
- └── `README.md          `# Документация проекта

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
