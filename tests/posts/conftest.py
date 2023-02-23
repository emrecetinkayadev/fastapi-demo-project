import pytest


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
    
@pytest.fixture
def post_in_get():
    return {
        "user_id": 1,
        "created_at": "2023-02-16",
        "title": "Updated Post",
        "content": "string",
        "id": 1
    }

@pytest.fixture
def post_in_put():
    return {
        "created_at": "2023-02-17",
        "title": "Updated Post",
        "content": "string updated",
        "id": 1
    }
