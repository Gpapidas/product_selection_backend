import os

ENVIRONMENT = os.environ.get("ENV_NAME", None)
FRONTEND_URL = os.environ.get("FRONTEND_URL", None)
DJANGO_ALLOWED_HOSTS_VAR = os.environ.get("DJANGO_ALLOWED_HOSTS")
HOST = os.environ.get("HOST", "http://localhost:8000")
