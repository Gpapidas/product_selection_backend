from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken


def handle_logout(refresh_token):
    try:
        token = RefreshToken(refresh_token)
        token.blacklist()
        return True
    except Exception:
        raise AuthenticationFailed("Invalid refresh token")
