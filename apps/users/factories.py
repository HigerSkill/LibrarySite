import factory
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    """Factory for generates test `User` instance."""

    username = factory.Faker("pystr")
    email = factory.Faker("email")

    class Meta:
        model = UserModel
