from rest_framework import serializers

from apps.authors.models import Author


class AuthorsSerializer(serializers.ModelSerializer):
    """Serializer for `Author` model."""
    class Meta:
        model = Author
        fields = (
            "first_name",
            "last_name",
            "surname",
        )
