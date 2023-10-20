from django.contrib.auth import get_user_model
from useless.serializers import RegistrationSerializer
from rest_framework import generics

User = get_user_model()


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
