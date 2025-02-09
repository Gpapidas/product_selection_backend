from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class BaseTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        """
        Perform class-level setup.
        Assumes the database is already seeded globally.
        """
        super().setUpClass()

        # Fetch test user (created via `test_seeds`)
        cls.test_user = User.objects.get(email="test@productselection.com")
        cls.test_password = "123test123" # nosec
        cls.login_url = reverse("users:login")

        # Generate JWT tokens initially
        cls.refresh_tokens()

    @classmethod
    def refresh_tokens(cls):
        """
        Generates fresh tokens for the test user.
        """
        refresh = RefreshToken.for_user(cls.test_user)
        cls.access_token = str(refresh.access_token)
        cls.refresh_token = str(refresh)

    def authenticate(self):
        """
        Generates fresh tokens for the user and applies authentication headers.
        """
        self.refresh_tokens()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def unauthenticate(self):
        """
        Removes authentication headers to simulate an unauthenticated request.
        """
        self.client.credentials()
