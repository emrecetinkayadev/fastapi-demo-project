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
