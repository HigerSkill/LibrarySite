from django.contrib import admin

from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    """Django admin for `Subscriber` model."""

    list_display = (
        "id",
        "email",
    )
    list_display_links = (
        "id",
        "email",
    )
    search_fields = (
        "first_name",
        "last_name",
        "surname",
        "email",
    )
    fields = (
        "first_name",
        "last_name",
        "surname",
        "email",
    )

