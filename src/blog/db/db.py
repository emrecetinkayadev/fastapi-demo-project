from datetime import datetime

user_table = [
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

post_table = [
    {
        "id": 1,
        "title": "Animals",
        "content": "",
        "created_at": datetime.strptime('01022023', "%d%m%Y").date(),
        "user_id": 1
    },
    {
        "id": 2,
        "title": "Travelling",
        "content": "",
        "created_at": datetime.strptime('03022023', "%d%m%Y").date(),
        "user_id": 2
    },
    {
        "id": 3,
        "title": "Where are we going?",
        "content": "",
        "created_at": datetime.strptime('10022023', "%d%m%Y").date(),
        "user_id": 1
    }
]
