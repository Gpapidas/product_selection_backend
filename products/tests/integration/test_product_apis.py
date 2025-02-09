from django.urls import reverse
from rest_framework import status

from products.models import Product
from shared.tests.base import BaseTestCase


class ProductAPITestCase(BaseTestCase):
    def setUp(self):
        """
        Set up test data before each test.
        """
        super().setUp()
        self.products_url = reverse("products:product-list")
        self.product = Product.objects.first()
        self.product_detail_url = reverse("products:product-detail", kwargs={"pk": self.product.id})
        self.product_select_url = reverse("products:product-select", kwargs={"pk": self.product.id})

    def test_get_all_products_success(self):
        """
        Test that an authenticated user can retrieve all products.
        """
        self.authenticate()
        response = self.client.get(self.products_url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["type"], "success")
        self.assertGreaterEqual(len(response.data["data"]), 1)  # Ensure products exist

    def test_get_all_products_unauthenticated(self):
        """
        Test that an unauthenticated user gets a 401 Unauthorized response.
        """
        self.unauthenticate()
        response = self.client.get(self.products_url, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data["type"], "client_error")
        self.assertEqual(response.data["errors"][0]["code"], "not_authenticated")

    def test_product_search_session_persistence(self):
        """
        Test session persistence by searching for a keyword, checking results,
        resetting the search, and verifying results.
        """
        self.authenticate()

        # Reset search first
        response = self.client.get(self.products_url, {"reset_search": "true"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Perform search
        response = self.client.get(self.products_url, {"search": "lord"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        initial_result_count = len(response.data["data"])

        # Request again without search, should return the same results (session persistence)
        response = self.client.get(self.products_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["data"]), initial_result_count)

        # Reset search and check if all products are returned again
        response = self.client.get(self.products_url, {"reset_search": "true"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        all_products_count = len(response.data["data"])
        self.assertGreater(all_products_count, initial_result_count)

    def test_get_single_product_success(self):
        """
        Test retrieving a single product successfully.
        """
        self.authenticate()
        response = self.client.get(self.product_detail_url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["type"], "success")
        self.assertEqual(response.data["data"]["id"], self.product.id)

    def test_get_single_product_unauthenticated(self):
        """
        Test that an unauthenticated user cannot retrieve a product.
        """
        self.unauthenticate()
        response = self.client.get(self.product_detail_url, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_single_product_not_found(self):
        """
        Test that a non-existing product returns a 404 Not Found.
        """
        self.authenticate()
        response = self.client.get(reverse("products:product-detail", kwargs={"pk": 99999}), format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_toggle_product_selection(self):
        """
        Test selecting and then deselecting a product, ensuring state updates correctly.
        """
        self.authenticate()

        # Ensure product is deselected at the start
        product_response = self.client.get(self.product_detail_url, format="json")
        self.assertEqual(product_response.status_code, status.HTTP_200_OK)
        self.assertEqual(product_response.data["type"], "success")
        self.assertEqual(product_response.data["data"]["selected"], False)

        # Select product
        select_response = self.client.post(self.product_select_url, format="json")
        self.assertEqual(select_response.status_code, status.HTTP_200_OK)
        self.assertEqual(select_response.data["type"], "success")
        self.assertEqual(select_response.data["data"]["selected"], True)

        # Fetch product and validate it is now selected
        product_response = self.client.get(self.product_detail_url, format="json")
        self.assertEqual(product_response.status_code, status.HTTP_200_OK)
        self.assertEqual(product_response.data["type"], "success")
        self.assertEqual(product_response.data["data"]["selected"], True)

        # Deselect product
        deselect_response = self.client.post(self.product_select_url, format="json")
        self.assertEqual(deselect_response.status_code, status.HTTP_200_OK)
        self.assertEqual(deselect_response.data["type"], "success")
        self.assertEqual(deselect_response.data["data"]["selected"], False)

        # Fetch product and validate it is now deselected
        product_response = self.client.get(self.product_detail_url, format="json")
        self.assertEqual(product_response.status_code, status.HTTP_200_OK)
        self.assertEqual(product_response.data["type"], "success")
        self.assertEqual(product_response.data["data"]["selected"], False)

    def test_select_product_unauthenticated(self):
        """
        Test that an unauthenticated user cannot select a product.
        """
        self.unauthenticate()
        response = self.client.post(self.product_select_url, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_select_product_not_found(self):
        """
        Test that selecting a non-existing product returns a 404 Not Found.
        """
        self.authenticate()
        response = self.client.post(reverse("products:product-select", kwargs={"pk": 99999}), format="json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
