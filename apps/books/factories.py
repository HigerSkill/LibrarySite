import factory
from factory import fuzzy

from ..authors.factories import AuthorFactory
from .models import Book
from .utils import Languages


class BookFactory(factory.django.DjangoModelFactory):
    """Factory for generates test `Book` instance."""

    author = factory.SubFactory(AuthorFactory)
    name = factory.Faker("pystr")
    language = fuzzy.FuzzyChoice(Languages)
    publication_year = fuzzy.FuzzyInteger(1, 2100)

    class Meta:
        model = Book
