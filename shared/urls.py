from django.urls import path

from shared.views import HelloWorldView

urlpatterns = [
    path("hello-world/", HelloWorldView.as_view(), name="hello-world"),
]
