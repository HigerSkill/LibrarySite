import factory

from .models import Subscriber


class SubscriberFactory(factory.django.DjangoModelFactory):
    """Factory for generates test `Subscriber` instance."""

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    surname = factory.Faker("first_name")
    email = factory.Faker("email")

    class Meta:
        model = Subscriber
