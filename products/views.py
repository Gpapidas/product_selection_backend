from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse, OpenApiExample
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from products.filters.product import ProductFilter
from products.models import Product
from products.serializers.product import ProductSerializer
from products.services.product.service import ProductService
from shared.utils.responses import SuccessResponse


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for listing and searching products.
    """
    queryset = Product.objects.all().order_by("-created_at")
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    http_method_names = ["get", "post"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_queryset(self):
        """
        Apply session-based search and sorting filters only for the 'list' action.
        """
        queryset = super().get_queryset()
        session = self.request.session

        if self.action == "list":
            reset_search = self.request.query_params.get("reset_search")

            # Reset search if requested
            if reset_search == "true":
                session["last_search_query"] = ""
                session.modified = True

            search_query = self.request.query_params.get("search", session.get("last_search_query", ""))

            # Update session with search query
            session["last_search_query"] = search_query
            session.modified = True

            return ProductFilter({"search": search_query}, queryset=queryset).qs

        return queryset

    @extend_schema(
        summary="Retrieve all products",
        description="Returns a paginated list of products. Supports search and sorting.",
        parameters=[
            OpenApiParameter(
                name="search",
                type=str,
                description="Search query for filtering products by name or description.",
                required=False
            ),
            OpenApiParameter(
                name="ordering",
                type=str,
                description="Sorting field (e.g., 'name', '-price', 'stock'). Default: '-created_at'",
                required=False
            ),
            OpenApiParameter(
                name="reset_search",
                type=bool,
                description="If 'true', resets the search session value.",
                required=False
            ),
        ],
        responses={
            200: OpenApiResponse(
                response=ProductSerializer(many=True),
                description="List of products",
                examples=[
                    OpenApiExample(
                        "Success Response",
                        value={
                            "type": "success",
                            "errors": [],
                            "detail": "Products retrieved successfully",
                            "data": [
                                {
                                    "id": 1,
                                    "name": "Abbey Road",
                                    "description": "The Beatles' legendary 1969 album...",
                                    "price": "29.99",
                                    "stock": 100,
                                    "created_at": "2025-02-07T12:34:56Z",
                                    "updated_at": "2025-02-07T12:34:56Z"
                                }
                            ]
                        }
                    )
                ]
            )
        }
    )
    def list(self, request, *args, **kwargs):
        """
        Override list to wrap response data in `products`.
        """
        response = super().list(request, *args, **kwargs)
        return SuccessResponse.format("Products retrieved successfully", data=response.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Override retrieve to wrap response data in `SuccessResponse`.
        """
        response = super().retrieve(request, *args, **kwargs)
        return SuccessResponse.format("Product retrieved successfully", data=response.data)

    @extend_schema(
        summary="Select/Deselect a product",
        description="Toggles the selection of a product. Selection is stored in session (to be implemented).",
        responses={
            200: OpenApiResponse(
                description="Product selection toggled",
                examples=[
                    OpenApiExample(
                        "Success Response",
                        value={
                            "type": "success",
                            "errors": [],
                            "detail": "Product 1 selection toggled (session logic pending)",
                            "data": None
                        }
                    )
                ]
            ),
            401: OpenApiResponse(
                description="Unauthorized",
                examples=[
                    OpenApiExample(
                        "Unauthorized Error",
                        value={
                            "type": "client_error",
                            "errors": [
                                {
                                    "code": "not_authenticated",
                                    "detail": "Authentication credentials were not provided."
                                }
                            ],
                            "detail": "Authentication credentials were not provided."
                        }
                    )
                ]
            ),
            404: OpenApiResponse(
                description="Product not found",
                examples=[
                    OpenApiExample(
                        "Not Found Error",
                        value={
                            "type": "client_error",
                            "errors": [
                                {
                                    "code": "not_found",
                                    "detail": "No product matches the given query."
                                }
                            ],
                            "detail": "No product matches the given query."
                        }
                    )
                ]
            )
        }
    )
    @action(detail=True, methods=["post"])
    def select(self, request, pk=None):
        """
        Mark or unmark a product as selected in session storage.
        """
        product = self.get_object()
        message, product = ProductService.product_selection(request.session, product)

        product_data = ProductSerializer(product, context={"request": request}).data

        return SuccessResponse.format(message, data=product_data)
