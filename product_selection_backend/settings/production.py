"""
Configuration for production development
"""
import os
import secrets

import dj_database_url

from product_selection_backend.settings.global_settings import DJANGO_ALLOWED_HOSTS_VAR, HOST, FRONTEND_URL

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    default=secrets.token_urlsafe(nbytes=64),
)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = DJANGO_ALLOWED_HOSTS_VAR.split(" ")

# CSRF and Cookie settings
CSRF_TRUSTED_ORIGINS = [HOST, FRONTEND_URL]
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Ensure HTTPS
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DATABASES = {
    "default": dj_database_url.config(
        env="DATABASE_URL",
        conn_max_age=600,
        ssl_require=True,
    )
}
