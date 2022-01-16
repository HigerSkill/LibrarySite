from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for User model."""
    class Meta:
        model = UserModel
        fields = (
            "username",
            "email",
        )
