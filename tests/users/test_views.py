import pytest
from fastapi.testclient import TestClient
from fastapi import status
from blog.main import app

client = TestClient(app)


def test_get_users__get_users__return_all_users(mocker, users):
    patched_get_all = mocker.patch('blog.users.views.get_all', return_value=users)
    response = client.get('/users')

    patched_get_all.assert_called_once()
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2
    assert response.json() == users


def test_get_user__get_user_return_user(mocker, user_in):
    user_id = 1
    patched_user = mocker.patch('blog.users.views.get', return_value=user_in)
    response = client.get(f'/users/{user_id}')

    patched_user.assert_called_once()
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == user_in


def test_get_user__get_user_not_found__return_not_found(mocker):
    user_id = 1
    patched_user = mocker.patch('blog.users.views.get', return_value=[])
    response = client.get(f'/users/{user_id}')

    patched_user.assert_called_once()
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': [{'msg': "User with this ID doesn't exist"}]}


def test_create_user__user_create__return_user(mocker, user_in):
    patched_create = mocker.patch('blog.users.views.create', return_value=user_in)
    response = client.post('/users', json=user_in)

    patched_create.assert_called_once()
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == user_in


def test_create_user__creation_failed__return_bad_request(mocker, user_in):
    patched_create = mocker.patch('blog.users.views.create', return_value=None)
    response = client.post('/users', json=user_in)

    patched_create.assert_called_once()
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {'detail': [{'msg': 'Error happened when trying to user creation'}]}


def test_update_user__user_updated__return_user(mocker, user_in):
    user_id = 1
    patched_get = mocker.patch('blog.users.views.get', return_value=user_in)
    patched_update = mocker.patch('blog.users.views.update', return_value=user_in)
    response = client.put(f'/users/{user_id}', json=user_in)

    patched_get.assert_called_once()
    patched_update.assert_called_once()
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == user_in


def test_update_user__update_failed__return_bad_request(mocker, user_in):
    user_id = 1
    patched_get = mocker.patch('blog.users.views.get', return_value=None)
    patched_update = mocker.patch('blog.users.views.update', return_value=None)
    response = client.put(f'/users/{user_id}', json=user_in)

    patched_get.assert_called_once()
    patched_update.assert_not_called()
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': [{"msg": "User with this ID doesn't exist"}]}


def test_delete_user__user_deleted__return_none(mocker, user_in):
    user_id = 1
    patched_get = mocker.patch('blog.users.views.get', return_value=user_in)
    response = client.delete(f'/users/{user_id}')

    patched_get.assert_called_once()
    assert response.status_code == status.HTTP_200_OK
    assert response.json() is None


def test_delete_user__delete_failed__return_not_found(mocker):
    user_id = 1
    patched_get = mocker.patch('blog.users.views.get', return_value=[])
    response = client.delete(f'/users/{user_id}')

    patched_get.assert_called_once()
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': [{'msg': "User with this ID doesn't exist"}]}
