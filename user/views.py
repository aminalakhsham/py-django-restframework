from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse
from rest_framework.exceptions import MethodNotAllowed

from .models import User
from .serializers import UserSerializer


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
