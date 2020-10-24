from datetime import date
import json

from django.urls import reverse
import pytest
from rest_framework import status

from book.constants import NEW_BOOKS
from book.models import Author, Book


@pytest.fixture
def set_up(db):
    today = date.today()
    author = Author.objects.create(name="kwon")
    Book.objects.create(
        name="테스트 책 이름",
        sub_name="테스트 서브 이름",
        type=NEW_BOOKS,
        author=author,
        description="abcde",
        price=1000,
        sale_price=1000,
        purchased_at=today,
        published_at=today,
    )


def test_book_list_should_return_200(set_up, client):
    # When: Call book_list
    response = client.get(reverse("book:list"))

    # Then: response status code is 200 OK
    assert response.status_code == status.HTTP_200_OK


# def test_book_list_should_return_response_content(set_up, client):
#     # When: Call book_list
#     response = client.get(reverse("book:list"))
#
#     # Then:
#     response = json.loads(response.content)[0]
#     assert response["name"] == "테스트 책 이름"
#     assert response["sub_name"] == "테스트 서브 이름"
#     assert response["type"] == NEW_BOOKS
#     assert response["author"] == set_up.author.id
#     assert response["description"] == "abcde"
#     assert response["price"] == "1000"
#     assert response["sale_price"] == "1000"
#     assert response["purchased_at"] == date.strftime(set_up.today, "%Y-%m-%d")
#     assert response["published_at"] == date.strftime(set_up.today, "%Y-%m-%d")
