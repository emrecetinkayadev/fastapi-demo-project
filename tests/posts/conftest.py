import pytest
from blog.posts.models import PostRead
from datetime import date


@pytest.fixture
def posts():
    return [
        {
            "id": 1,
            "title": "Animals",
            "content": "",
            "created_at": "2023-01-01",
            "user_id": 1
        },
        {
            "id": 2,
            "title": "Travelling",
            "content": "",
            "created_at": "2023-01-20",
            "user_id": 2
        },
        {
            "id": 3,
            "title": "Future",
            "content": "",
            "created_at": "2023-02-13",
            "user_id": 1
        },
        {
            "id": 4,
            "title": "Future",
            "content": "",
            "created_at": "2023-02-16",
            "user_id": 3
        }
    ]


@pytest.fixture
def post_in():
    return {
            "title": "New Post",
            "content": "",
            "created_at": "2023-02-16",
            "user_id": 1
        }
