from django.contrib.postgres.fields import CICharField
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


class Subscriber(models.Model):
    """Model that represents the subscribers."""

    first_name = models.CharField(
        verbose_name=_("First Name"),
        max_length=80,
    )
    last_name = models.CharField(
        verbose_name=_("Last Name"),
        max_length=80,
    )
    surname = models.CharField(
        verbose_name=_("Surname"),
        max_length=80,
    )
    email = CICharField(
        verbose_name=_("Email"),
        max_length=80,
        validators=[validators.validate_email],
    )

    class Meta:
        verbose_name = _("Subscriber")
        verbose_name_plural = _("Subscribers")

    def __str__(self):
        return f"Subscriber {self.first_name} {self.last_name} {self.surname}"
