from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from shared.utils.validations import is_valid_email
from .helpers import initialize_user_session

User = get_user_model()


def handle_login(session, email, password):
    if not email or not password:
        raise ValidationError("Email and password required")

    if not is_valid_email(email):
        raise ValidationError("Email is invalid")

    user, created = User.objects.get_or_create(email=email, defaults={"username": email})

    if created:
        user.set_password(password)
        user.save()

    refresh = RefreshToken.for_user(user)
    update_last_login(None, user)

    initialize_user_session(session)

    return user, str(refresh.access_token), str(refresh)
