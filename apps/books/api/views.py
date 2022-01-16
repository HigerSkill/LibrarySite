from django.utils.timezone import now
from rest_framework import viewsets

from apps.books.api.serializers import BooksSerializer
from apps.books.models import Book


class BooksViewSet(viewsets.ModelViewSet):
    """ViewSet for `Book` model."""
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    search_fields = (
        "name",
        "language",
        "publication_year",
    )

    def get_queryset(self):
        """Return queryset without future books for non staff users."""
        queryset = super().get_queryset()

        if not bool(self.request.user and self.request.user.is_staff):
            # Hide books which has publication year in future
            # for non staff users
            queryset = queryset.filter(publication_year__lte=now().year)

        return queryset
