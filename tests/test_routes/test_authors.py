from tests.config_test import client
from fastapi import status

create_author = {
    "name": "Asad Ali"
}

update_author = {
    "name": "Ali"
}

author_id = 1


def test_create_author():
    response = client.post(
        "/authors",
        json=create_author
    )
    assert response.status_code == status.HTTP_201_CREATED


def test_get_author_by_id():
    response = client.get('/authors/{}'.format(author_id))
    assert response.status_code == status.HTTP_200_OK


def test_update_author():
    response = client.patch('/authors/{}'.format(author_id), json=update_author)
    assert response.status_code == status.HTTP_200_OK


def test_delete_author():
    response = client.delete('/authors/{}'.format(author_id))
    assert response.status_code == status.HTTP_200_OK