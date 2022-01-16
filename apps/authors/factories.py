import factory

from .models import Author


class AuthorFactory(factory.django.DjangoModelFactory):
    """Factory for generates test `Author` instance."""

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    surname = factory.Faker("first_name")

    class Meta:
        model = Author
