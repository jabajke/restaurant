from django.urls import path, include
from rest_framework import routers
from useless.views import UserCreateAPIView

urlpatterns = [
    path("signup/", UserCreateAPIView.as_view(), name="signup")
]
