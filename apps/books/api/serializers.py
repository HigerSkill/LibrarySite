from rest_framework import serializers

from apps.books.models import Book


class BooksSerializer(serializers.ModelSerializer):
    """Serializer for `Book` model."""
    class Meta:
        model = Book
        fields = (
            "author",
            "name",
            "language",
            "publication_year",
        )
