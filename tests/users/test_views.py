import pytest
from fastapi.testclient import TestClient
from fastapi import status
from blog.main import app

client = TestClient(app)


def get_users__get_users__return_all_users(mocker, users):
    patched_get_all = mocker.patch('blog.users.views.get_all', return_value=users)
    response = client.get('/users')

    patched_get_all.assert_called_once()
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2
    assert response.json() == users


def get_user__get_user_return_user(mocker, user_in):
    user_id = 1
    patched_user = mocker.patch('blog.users.views.get', return_value=user_in)
    response = client.get(f'/users/{user_id}')

    patched_user.assert_called_once()
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1
    assert response.json() == user_in


def get_user__get_user_not_found__return_not_found(mocker):
    user_id = 1
    patched_user = mocker.patch('blog.users.views.get', return_value=[])
    response = client.get(f'/users/{user_id}')

    patched_user.assert_called_once()
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert len(response.json()) == 0
    assert response.json is None
