"""
Configuration for local development
"""
import os

from .base import BASE_DIR, INSTALLED_APPS, MIDDLEWARE, LOGGING

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-fuv5#wl!*9)ahi^6z!*@2nzd(+mhli^yjsvpyw@dj#zt@6yv8t")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get("DEBUG", default=1))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", default="127.0.0.1").split(" ")

INSTALLED_APPS = INSTALLED_APPS + []  # Installed apps only for local dev
MIDDLEWARE = MIDDLEWARE + []  # Middlewares only for local dev
LOGGING["loggers"]["nplusone"] = {
    "level": "DEBUG",
    "handlers": ["console_debug"],
}

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("POSTGRES_DB", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("POSTGRES_USER", "user"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "password"),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}

CORS_ALLOW_ALL_ORIGINS = True
