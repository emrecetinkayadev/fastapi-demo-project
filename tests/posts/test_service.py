import pytest
from fastapi import status
from blog.posts.models import PostCreate
from blog.posts.service import get


def test_get__post_found__return_post(posts, mocker):
    mocker.patch('blog.posts.service.post_table', posts)
    res = get(post_id=1)

    assert res == posts[0]


def test_get_all__post_not_found__return_posts(posts, mocker):
    mocker.patch('blog.posts.service.post_table', posts)
    res = get(post_id=5)

    assert res is None

