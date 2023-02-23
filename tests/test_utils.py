import pytest
from datetime import datetime
from blog.utils import max_id

post_table = [
    {
        "id": 1,
    },
    {
        "id": 8,
    },
    {
        "id": 3,
    }
]


def test_utils__returns_max_id():
    assert max_id(post_table) == 8
