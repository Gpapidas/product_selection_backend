from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenRefreshView

from shared.utils.responses import SuccessResponse
from users.serializers.user import UserSerializer
from .services.auth.service import AuthService


class LoginView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        operation_id="login_user",
        summary="Log in or auto-register a user",
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "email": {"type": "string", "format": "email", "description": "User email"},
                    "password": {"type": "string", "description": "User password"},
                },
                "required": ["email", "password"],
            }
        },
        responses={
            200: OpenApiResponse(
                response=UserSerializer,
                description="Successful login",
                examples=[
                    OpenApiExample(
                        "Success Response",
                        value={
                            "type": "success",
                            "errors": [],
                            "detail": "User logged in successfully",
                            "data": {
                                "user": {
                                    "id": 1,
                                    "email": "test@example.com",
                                    "username": "test123",
                                    "first_name": "John",
                                    "last_name": "Doe",
                                    "date_joined": "2024-02-06T12:34:56Z",
                                },
                                "access_token": "JWT_ACCESS_TOKEN",
                                "refresh_token": "JWT_REFRESH_TOKEN",
                            }
                        }
                    )
                ]
            ),
        }
    )
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        session = request.session

        user, access_token, refresh_token = AuthService.login(session, email, password)

        return SuccessResponse.format(
            message="User logged in successfully",
            data={
                "user": UserSerializer(user).data,
                "access_token": access_token,
                "refresh_token": refresh_token
            }
        )


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="logout_user",
        summary="Log out and blacklist refresh token",
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "refresh_token": {"type": "string", "description": "User's refresh token"},
                },
                "required": ["refresh_token"],
            }
        },
        responses={
            200: OpenApiResponse(
                description="Successful logout",
                examples=[
                    OpenApiExample(
                        "Success Response",
                        value={
                            "type": "success",
                            "errors": [],
                            "detail": "Logged out successfully",
                            "data": None
                        }
                    )
                ]
            )
        }
    )
    def post(self, request):
        refresh_token = request.data.get("refresh_token")
        session = request.session

        AuthService.logout(session, refresh_token)

        return SuccessResponse.format(message="Logged out successfully")


class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]

    @extend_schema(
        operation_id="refresh_token",
        summary="Refresh the access token using a refresh token",
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "refresh": {"type": "string", "description": "The refresh token"},
                },
                "required": ["refresh"],
            }
        },
        responses={
            200: OpenApiResponse(
                description="New access token",
                examples=[
                    OpenApiExample(
                        "Success Response",
                        value={
                            "type": "success",
                            "errors": [],
                            "detail": "Access token refreshed successfully",
                            "data": {
                                "access": "NEW_JWT_ACCESS_TOKEN",
                                "refresh": "NEW_REFRESH_TOKEN_IF_ROTATE_ENABLED"
                            }
                        }
                    )
                ]
            ),
            401: OpenApiExample(
                "Invalid refresh token",
                value={
                    "type": "error",
                    "errors": [{"code": "invalid_token", "detail": "Token is invalid or expired"}],
                    "detail": "Token is invalid or expired"
                },
            ),
        },
    )
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        # Modify response to fit our success format
        if response.status_code == 200:
            return SuccessResponse.format(
                message="Access token refreshed successfully",
                data=response.data
            )

        return response


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="get_current_user",
        summary="Get the current authenticated user's details",
        responses={
            200: OpenApiResponse(
                response=UserSerializer,
                description="Current user details",
                examples=[
                    OpenApiExample(
                        "Success Response",
                        value={
                            "type": "success",
                            "errors": [],
                            "detail": "Current user retrieved successfully",
                            "data": {
                                "id": 1,
                                "email": "test@example.com",
                                "username": "test123",
                                "first_name": "John",
                                "last_name": "Doe",
                                "date_joined": "2024-02-06T12:34:56Z",
                            }
                        }
                    )
                ]
            )
        }
    )
    def get(self, request):
        user_data = UserSerializer(request.user).data
        return SuccessResponse.format(message="Current user retrieved successfully", data=user_data)
