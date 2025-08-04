#!/bin/bash
set -e  # Прерывание при ошибках

# Выполнение миграций
echo "Applying database migrations..."
python manage.py migrate

# Сбор статики (если не сделана при сборке образа)
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Запуск основной команды (из CMD или compose)
exec "$@"
