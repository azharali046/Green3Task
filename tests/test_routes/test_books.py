from tests.config_test import client
from fastapi import status

create_book = {
    "name": "Red Flowers",
    "author_id": 1
}

update_book = {
    "name": "Flowers",
    "author_id": 1
}
author_id = 1
book_id = 1


def test_create_book():
    response = client.post(
        "/books",
        json=create_book
    )
    assert response.status_code == status.HTTP_201_CREATED


def test_get_book_by_author_id():
    response = client.get('/books?author_id={}'.format(book_id))
    assert response.status_code == status.HTTP_200_OK


def test_get_book_by_id():
    response = client.get('/books/{}'.format(book_id))
    assert response.status_code == status.HTTP_200_OK


def test_update_book():
    response = client.patch('/books/{}'.format(book_id), json=update_book)
    assert response.status_code == status.HTTP_200_OK


def test_delete_book():
    response = client.delete('/books/{}'.format(book_id))
    assert response.status_code == status.HTTP_200_OK
