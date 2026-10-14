─$ cat Dockerfile                                                                                                           130 ↵
FROM python:3.14-slim

copy --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/opt/venv

WORKDIR /app


─$ cat compose.yaml                                                                                                         130 ↵
services:
  db:
    image: postgres:18-alpine
    env_file: .env
    volumes:
      - pgdata:/var/lib/postgresql

  mailpit:
    image: axllent/mailpit
    ports:
      - "8025:8025"

  web:
    build: .
    command: uv run python manage.py runserver 0.0.0.0:8000
    env_file: .env
    volumes:
      - .:/app
      - venv:/opt/venv
    ports:
      - "8000:8000"
    depends_on:
      - db
      - mailpit

volumes:
  pgdata:
  venv:


─$ cat .env        
SECRET_KEY=django-insecure-troque-esta-chave
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
POSTGRES_DB=empresa
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
EMAIL_HOST=mailpit
EMAIL_PORT=1025


╰─$ cat pyproject.toml 
[project]
name = "empresa"
version = "0.1.0"
requires-python = ">=3.14"
dependencies = [
    "django>=6.1.2",
    "psycopg[binary]>=3.3.6",
    "python-decouple>=3.8",
]



docker compose run --rm web uv init --bare --name empresa
docker compose run --rm web uv add django 'psycopg[binary]' python-decouple
cat pyproject.toml
docker compose run --rm web uv run django-admin startproject config .
docker compose run --rm web uv run python manage.py startapp core
docker compose run --rm web uv run python manage.py startapp accounts
docker compose run --rm web uv run python manage.py startapp person

nvim config/settings.py

mkdir -p core/templates/core

mkdir -p core/templates/core
sudo nvim core/templates/core/index.html
sudo nvim core/templates/403.html
sudo nvim config/urls.py
sudo mkdir -p accounts/templates/registration
sudo nvim accounts/templates/registration
sudo nvim accounts/templates/registration/login.html
sudo nvim accounts/templates/registration/password_reset_form.html
sudo nvim accounts/templates/registration/password_reset_reset_done.html
sudo nvim accounts/templates/registration/password_reset_confirm.html     





