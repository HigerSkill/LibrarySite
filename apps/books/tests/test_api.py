from functools import partial

import pytest
from freezegun import freeze_time
from rest_framework import status
from rest_framework.reverse import reverse_lazy

from apps.books.factories import BookFactory


def get_proposal_books_url(action_name: str):
    """Get url for books list."""
    return reverse_lazy(f"api:book-{action_name}")


get_list_books_url = partial(
    get_proposal_books_url, action_name="list",
)


@freeze_time("2022-01-01")
@pytest.mark.parametrize(
    "test_user",
    [pytest.lazy_fixture("user"), pytest.lazy_fixture("admin_user")],
)
def test_hide_future_books_from_non_admin(api_client, test_user):
    """Test that non admins can't see books published after the current year.

    """
    book = BookFactory(publication_year=2000)
    future_book = BookFactory(publication_year=2023)

    api_client.force_authenticate(test_user)
    response = api_client.get(get_list_books_url())

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2 if test_user.is_staff else 1

    assert response.data[0]["publication_year"] == book.publication_year

    if test_user.is_staff:
        assert response.data[1]["publication_year"] == \
               future_book.publication_year
