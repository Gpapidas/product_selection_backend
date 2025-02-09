from .handlers.login_handler import handle_login
from .handlers.logout_handler import handle_logout


class AuthService:
    @staticmethod
    def login(email, password):
        return handle_login(email, password)

    @staticmethod
    def logout(refresh_token):
        return handle_logout(refresh_token)
