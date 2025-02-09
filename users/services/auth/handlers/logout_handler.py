from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from .helpers import clear_user_session


def handle_logout(session, refresh_token):
    try:
        token = RefreshToken(refresh_token)
        token.blacklist()
        clear_user_session(session)
        return True
    except Exception:
        raise AuthenticationFailed("Invalid refresh token")
