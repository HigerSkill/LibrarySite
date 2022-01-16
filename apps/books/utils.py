from django.db import models
from django.utils.translation import gettext_lazy as _


class Languages(models.TextChoices):
    """Language choices."""
    RU = "ru", _("Russian")
    EN = "en", _("English")
    FR = "fr", _("French")
    DE = "de", _("German")
