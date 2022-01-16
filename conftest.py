import pytest
from django.conf import settings
from rest_framework.test import APIClient

from apps.users.factories import UserFactory

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """Allow all tests to access DB."""


@pytest.fixture(scope="function")
def api_client() -> APIClient:
    """Create API client."""
    return APIClient()


@pytest.fixture(scope="session")
def user(django_db_setup, django_db_blocker):
    """Module-level fixture for user."""
    with django_db_blocker.unblock():
        created_user = UserFactory()
        yield created_user
        created_user.delete()
