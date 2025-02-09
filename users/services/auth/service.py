from .handlers.login_handler import handle_login
from .handlers.logout_handler import handle_logout


class AuthService:
    @staticmethod
    def login(session, email, password):
        return handle_login(session, email, password)

    @staticmethod
    def logout(session, refresh_token):
        return handle_logout(session, refresh_token)
