import pytest
from fastapi.testclient import TestClient
from fastapi import status
from blog.main import app
from blog.posts.models import PostCreate

client = TestClient(app)


def test_get_posts__posts_found__return_posts(posts, mocker):
    patched_get_all = mocker.patch('blog.posts.views.get_all', return_value=posts)
    response = client.get("/posts")

    patched_get_all.assert_called_once()
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 4
    assert response.json() == posts


def test_get_posts__no_posts_found__return_empty_list(mocker):
    patched_get_all = mocker.patch('blog.posts.views.get_all', return_value=[])
    response = client.get("/posts")

    patched_get_all.assert_called_once()
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []


def test_create_post__post_created__return_created_post(post_in, mocker):
    post_response = post_in.copy()
    post_response["id"] = 5
    patched_create = mocker.patch('blog.posts.views.create', return_value=post_response)
    response = client.post("/posts", json=post_in)

    patched_create.assert_called_once()
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == post_response


def test_create_post__creation_failed__bad_request(post_in, mocker):
    patched_create = mocker.patch('blog.posts.views.create', return_value=None)
    response = client.post("/posts", json=post_in)

    patched_create.assert_called_once()
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {'detail': [{'msg': 'Error happened in creating post.'}]}


def test_update_post__post_updated__return_updated_post(post_in_put, post_in_get, mocker):
    post_id = 1
    updated_data = post_in_put.copy() 
    updated_data["user_id"] = post_in_get["user_id"]

    patched_get = mocker.patch('blog.posts.views.get', return_value=post_in_get)
    patched_update = mocker.patch('blog.posts.views.update', return_value=updated_data)
    response_update = client.put(f"/posts/{post_id}", json=post_in_put)

    patched_get.assert_called_once()
    patched_update.assert_called_once()
    assert response_update.status_code == status.HTTP_200_OK
    assert response_update.json() == updated_data


def test_update_post__post_cannot_find__return_not_found(mocker):
    post_id = 1
    patched_get = mocker.patch('blog.posts.views.get', return_value=None)
    response = client.get(f"/posts/{post_id}")

    patched_get.assert_called_once()
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': [{"msg": "Post with this id doesn't exist"}]}


def test_delete_post__post_connot_find__return_not_found(mocker):
    post_id = 1
    patched_get = mocker.patch('blog.posts.views.get', return_value=None)
    response = client.get(f"/posts/{post_id}")

    patched_get.assert_called_once()
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail":[{"msg": "Post with this id doesn't exist"}]}


def test_delete_post__post_deleted__return_success_response(mocker, post_in_get):
    post_id = 1
    patched_get = mocker.patch('blog.posts.views.get', return_value=post_in_get)
    patched_delete = mocker.patch('blog.posts.views.delete', return_value=None)
    response = client.delete(f"/posts/{post_id}")

    patched_get.assert_called_once()
    patched_delete.assert_called_once()
    assert response.json() is None
    assert response.status_code == status.HTTP_200_OK