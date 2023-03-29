import pytest
from fastapi import status
from fastapi.testclient import TestClient

from blog.main import app

client = TestClient(app)


def test_get_post__post_not_found__return_error_message(mocker):
    post_id = 100
    patched_get = mocker.patch('blog.posts.views.get', return_value=None)
    response = client.get(f"/posts/{post_id}")
    data = response.json()

    patched_get.assert_called_once()
    assert data == {'detail': [{'msg': "Post with this id doesn't exist"}]}
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_get_posts__no_posts_found__return_empty_list():
    response = client.get("/posts")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []


def test_create_post__post_created__return_created_post(post_in):
    response = client.post("/posts", json=post_in)
    data = response.json()

    assert response.status_code == status.HTTP_200_OK, response.text
    assert post_in["title"] == data["title"]
    assert post_in["content"] == data["content"]
    assert post_in["user_id"] == data["user_id"]


def test_get__post_found__return_post():
    post_id = 1
    response = client.get(f"/posts/{post_id}")
    data = response.json()

    assert response.status_code == status.HTTP_200_OK, response.text
    assert data["title"] == "New Post"
    assert data["content"] == ""
    assert data["user_id"] == 1
    assert data["id"] == 1


def test_get_posts__posts_found__return_posts():
    response = client.get("/posts")
    data = response.json()

    assert data[0]["title"] == "New Post"
    assert data[0]["content"] == ""
    assert data[0]["user_id"] == 1
    assert data[0]["id"] == 1
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) >= 1


def test_create_post__creation_failed__bad_request(post_in, mocker):
    patched_create = mocker.patch('blog.posts.views.create', return_value=None)
    response = client.post("/posts", json=post_in)

    patched_create.assert_called_once()
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {'detail': [{'msg': 'Error happened when trying to creating post.'}]}


def test_update_post__post_updated__return_updated_post(post_in_put, post_updated):
    post_id = 1
    response_update = client.put(f"/posts/{post_id}", json=post_in_put)

    assert response_update.status_code == status.HTTP_200_OK
    assert response_update.json() == post_updated


def test_update_post__post_cannot_find__return_not_found(mocker):
    post_id = 1
    patched_get = mocker.patch('blog.posts.views.get', return_value=None)
    response = client.get(f"/posts/{post_id}")

    patched_get.assert_called_once()
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': [
        {"msg": "Post with this id doesn't exist"}]}


def test_delete_post__post_connot_find__return_not_found(mocker):
    post_id = 1
    patched_get = mocker.patch('blog.posts.views.get', return_value=None)
    response = client.get(f"/posts/{post_id}")

    patched_get.assert_called_once()
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": [
        {"msg": "Post with this id doesn't exist"}]}


def test_delete_post__post_deleted__return_success_response():
    post_id = 1
    response = client.delete(f"/posts/{post_id}")

    assert response.json() is None
    assert response.status_code == status.HTTP_200_OK
