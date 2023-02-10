from blog.db.db import user_table
from blog.users.models import UserBase, User, UserCreate
import typing as t
from blog.utils import max_id, hash_password


def get_all() -> t.List[t.Optional[User]]:
    return user_table


def get(user_id) -> t.Optional[User]:
    usr = None
    for user in user_table:
        if user["id"] == user_id:
            usr = user
    return usr


def create(user_in: UserCreate) -> t.Optional[User]:
    new_user_id = max_id(user_table) + 1
    new_user = user_in.dict(exclude_unset=True)
    new_user["id"] = new_user_id
    new_user["password"] = hash_password(password=new_user["password"])
    user_table.append(new_user)
    return new_user
