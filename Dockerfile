FROM python:3.11.9-slim

WORKDIR /app

ENV POETRY_VERSION=2.1.1 \
    POETRY_HOME=/opt/poetry \
    POETRY_NO_VIRTUALENVS=1 \
    POETRY_VIRTUALENVS_CREATE=false

RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock ./

RUN poetry install --only=main --no-root --sync

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


