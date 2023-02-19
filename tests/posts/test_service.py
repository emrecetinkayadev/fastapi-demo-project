import pytest
from fastapi import status
from blog.posts.models import PostCreate
from blog.posts.service import get, get_all, get_posts_by_user_id, create, update, delete
from blog.posts.models import PostCreate, PostUpdate
import datetime

def test_get__post_found__return_post(posts, mocker):
    mocker.patch('blog.posts.service.post_table', posts)
    res = get(post_id=1)

    assert res == posts[0]

def test_get__post_not_found__return_none(mocker):
    mocker.patch('blog.posts.service.post_table', [])
    res = get(post_id=1)

    assert res is None


def test_get_all__post_not_found__return_none(posts, mocker):
    mocker.patch('blog.posts.service.post_table', posts)
    res = get(post_id=5)

    assert res is None


def test_get_all__post_found__return_posts(posts, mocker):
    mocker.patch('blog.posts.service.post_table', posts)
    res = get_all()

    assert res is posts

# Not sure if this test is correct or not.
def test_get_posts_by_user_id__post_found__return_posts(posts, mocker):
    mocker.patch('blog.posts.service.post_table', posts)
    res = get_posts_by_user_id(user_id=1)
    user_posts = [post for post in posts if post["user_id"] == 1]

    assert res == user_posts


def test_get_posts_by_user_id__post_not_found__return_empty_list(mocker):
    mocker.patch('blog.posts.service.post_table', [])
    res = get_posts_by_user_id(user_id=1)

    assert res == []


def test_create__new_post__return_new_post(mocker, post_in, posts):
    mocker.patch('blog.posts.service.post_table', posts)

    post_in_obj = PostCreate(**post_in)
    post = create(post_in=post_in_obj)

    expected_post = post_in_obj.dict(exclude_unset=True)
    expected_post['id'] = 5

    assert post == expected_post


def test_update__update_post__return_updated_post(mocker, post_in_put, posts, post_in):
    mocker.patch('blog.posts.service.post_table', posts)

    post_put_obj = PostUpdate(**post_in_put)
    post = update(update_data=post_put_obj, get_post=post_in)

    expected_post = post_put_obj.dict(exclude_unset=True)
    expected_post['user_id'] = 1

    assert post == expected_post


def test_delete__delete_post__return_none(mocker,posts):
    mocker.patch('blog.posts.service.post_table', posts)
    res = delete(post_id=1)
    assert res is None
