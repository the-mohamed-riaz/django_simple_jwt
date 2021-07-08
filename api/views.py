from django.shortcuts import render
from rest_framework import viewsets

from api.models import User
from api.serializer import UserSerializer

from rest_framework.permissions import AllowAny
from api.permission import IsLoggedInUserOrAdmin, IsAdminUser

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_class = []
        if self.action == 'create':
            permission_class = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_class = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_class = [IsAdminUser]
        return [permission() for permission in permission_class]
