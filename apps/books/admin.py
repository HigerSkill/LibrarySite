from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Django admin for `Book` model."""

    list_display = (
        "id",
        "author",
        "name",
        "language",
        "publication_year",
    )
    list_display_links = (
        "id",
        "name",
    )
    search_fields = (
        "id",
        "author",
        "name",
        "language",
        "publication_year",
    )
    fields = (
        "author",
        "name",
        "language",
        "publication_year",
    )
