import pytest


@pytest.fixture
def users():
    return [
        {
            "id": 1,
            "username": "user_1",
            "email": "user_1@gmail.com",
            "password": "",
        },
        {
            "id": 2,
            "username": "user_2",
            "email": "user_2@gmail.com",
            "password": ""
        }
    ]


@pytest.fixture
def user_in():
    return {
        "id": 1,
        "username": "user_1",
        "email": "user_1@gmail.com",
        "password": "",
    }
