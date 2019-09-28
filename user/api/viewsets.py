from django.shortcuts import get_object_or_404

from user.models import User
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserEmailViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer