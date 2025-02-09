from django.urls import reverse
from rest_framework import status

from shared.tests.base import BaseTestCase


class UserAPITestCase(BaseTestCase):
    def setUp(self):
        """
        Set up test data before each test.
        """
        super().setUp()
        self.current_user_url = reverse("users:current-user")

    def test_get_current_user_success(self):
        """
        Test that an authenticated user can retrieve their own details.
        """
        self.authenticate()
        response = self.client.get(self.current_user_url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["type"], "success")
        self.assertEqual(response.data["data"]["email"], self.test_user.email)
        self.assertEqual(response.data["data"]["username"], self.test_user.username)

    def test_get_current_user_unauthenticated(self):
        """
        Test that an unauthenticated user gets a 401 Unauthorized response.
        """
        self.unauthenticate()
        response = self.client.get(self.current_user_url, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data["type"], "client_error")
        self.assertEqual(response.data["errors"][0]["code"], "not_authenticated")
