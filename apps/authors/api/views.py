from rest_framework import viewsets

from apps.authors.api.serializers import AuthorsSerializer
from apps.authors.models import Author


class AuthorsViewSet(viewsets.ModelViewSet):
    """ViewSet for `Author` model."""
    queryset = Author.objects.all()
    serializer_class = AuthorsSerializer
    search_fields = (
        "first_name",
        "last_name",
        "surname",
    )
