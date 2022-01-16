from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuthorsAppConfig(AppConfig):
    """Default configuration for `Author` app."""

    name = "apps.authors"
    verbose_name = _("Author")
