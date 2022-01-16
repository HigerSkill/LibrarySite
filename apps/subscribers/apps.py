from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SubscribersAppConfig(AppConfig):
    """Default configuration for `Subscriber` app."""

    name = "apps.subscribers"
    verbose_name = _("Subscriber")
