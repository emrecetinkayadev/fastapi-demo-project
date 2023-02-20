import pytest
from blog.users.service import get_all, get, create, update, delete
from blog.users.models import UserCreate, UserUpdate


def test_get_all__users_found__return_all_users(mocker, users):
    mocker.patch('blog.users.service.user_table', users)
    res = get_all()

    assert res == users


def test_get_all__users_not_found__return_none(mocker):
    mocker.patch('blog.users.service.user_table', None)
    res = get_all()

    assert res == None


def test_get__user_not_found__return_none(users, mocker):
    mocker.patch('blog.users.service.user_table', users)
    res = get(user_id=5)

    assert res is None


def test_get__user_found__return_user(users, user_in, mocker):
    mocker.patch('blog.posts.service.post_table', users)
    res = get(user_id=1)

    assert res == user_in


def test_create__create_succesful__return_new_user(mocker, users, user_post):
    mocker.patch('blog.posts.service.post_table', users)
    mocker.patch('blog.posts.service.max_id', 3)

    new_user = user_post.copy()
    new_user['id'] = 3
    new_user['password'] = "5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5"

    res = create(user_in=UserCreate(**user_post))

    assert res == new_user


def test_update__update_succesful__return_updated_user(mocker, users, user_post):
    user_id = 1
    mocker.patch('blog.posts.service.post_table', users)

    updated_user = user_post.copy()
    updated_user['id'] = user_id
    updated_user['password'] = "5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5"

    res = update(user_id=user_id, user_in=UserUpdate(**user_post))

    assert res == updated_user


def test_delete__delete_succesful__return_none(mocker, users):
    user_id = 1
    mocker.patch('blog.posts.service.post_table', users)
    res = delete(user_id=user_id)

    assert res is None
