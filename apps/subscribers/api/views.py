from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from apps.subscribers.api.serializers import SubscriberSerializer
from apps.subscribers.models import Subscriber


class SubscribersViewSet(viewsets.ModelViewSet):
    """ViewSet for `Subscriber` model."""
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    permission_classes = (IsAdminUser,)
    search_fields = (
        "first_name",
        "last_name",
        "surname",
        "email",
    )

