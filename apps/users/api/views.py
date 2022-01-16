from django.contrib.auth import get_user_model
from rest_framework import viewsets

from apps.users.api.serializers import UsersSerializer

UserModel = get_user_model()


class UsersViewSet(viewsets.ModelViewSet):
    """ViewSet for `User` model."""
    queryset = UserModel.objects.all()
    serializer_class = UsersSerializer
