from rest_framework import serializers

from apps.subscribers.models import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    """Serializer for `Subscriber` model."""
    class Meta:
        model = Subscriber
        fields = (
            "first_name",
            "last_name",
            "surname",
            "email",
        )
