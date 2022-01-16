from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.books.utils import Languages


class Book(models.Model):
    """Model that represents the authors."""

    author = models.ForeignKey(
        to="authors.Author",
        verbose_name=_("Author"),
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=80,
    )
    language = models.CharField(
        verbose_name=_("Language"),
        max_length=7,
        choices=Languages.choices,
    )
    publication_year = models.PositiveSmallIntegerField(
        verbose_name=_("Publication Year"),
    )

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __str__(self):
        return f"Book {self.name}"
