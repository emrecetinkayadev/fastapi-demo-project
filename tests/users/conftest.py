import pytest


@pytest.fixture
def users():
    return [
        {
            "id": 1,
            "username": "user_1",
            "email": "user_1@gmail.com",
        },
        {
            "id": 2,
            "username": "user_2",
            "email": "user_2@gmail.com",
        }
    ]


@pytest.fixture
def user_in():
    return {
        "id": 1,
        "username": "user_1",
        "email": "user_1@gmail.com",
    }


@pytest.fixture
def user_post():
    return {
        "username": "user_1",
        "email": "user_1@gmail.com",
        "password": 12345
    }
