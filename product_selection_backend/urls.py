"""
URL configuration for product_selection_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from product_selection_backend.settings.global_settings import ENVIRONMENT

API_PATH = "api/"
API_V1_PATH = API_PATH + "v1/"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f"{API_V1_PATH}general/", include(("shared.urls", "shared"), namespace='shared')),
    path(f"{API_V1_PATH}auth/", include(("users.urls", "users"), namespace='users')),
]

if ENVIRONMENT == "development":
    from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

    urlpatterns += path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    urlpatterns += path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    urlpatterns += path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
