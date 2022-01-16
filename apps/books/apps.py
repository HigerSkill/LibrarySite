from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BooksAppConfig(AppConfig):
    """Default configuration for `Book` app."""

    name = "apps.books"
    verbose_name = _("Book")

    def ready(self):
        from . import signals  # noqa
