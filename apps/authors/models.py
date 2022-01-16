from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    """Model that represents the authors."""

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

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return f"Author {self.first_name} {self.last_name} {self.surname}"
