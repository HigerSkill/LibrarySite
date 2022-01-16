from django.contrib import admin

from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Django admin for `Author` model."""

    list_display = (
        "id",
        "first_name",
        "last_name",
        "surname",
    )
    list_display_links = (
        "id",
        "first_name",
    )
    search_fields = (
        "id",
        "first_name",
        "last_name",
        "surname",
    )
    fields = (
        "first_name",
        "last_name",
        "surname",
    )
