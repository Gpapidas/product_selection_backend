from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


def handle_login(email, password):
    if not email or not password:
        raise ValueError("Email and password required")

    user, created = User.objects.get_or_create(email=email, defaults={"username": email})

    if created:
        user.set_password(password)
        user.save()

    refresh = RefreshToken.for_user(user)
    update_last_login(None, user)

    return user, str(refresh.access_token), str(refresh)
