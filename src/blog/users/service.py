from src.blog.db.db import user_table
from src.blog.users.models import User, UserCreate, UserUpdate, UserRead
import typing as t
from src.blog.db.database import db
from src.blog.db.db_models import User as User_db


def get_all() -> t.List[t.Optional[UserRead]]:
    user_table = db.query(User_db).all()
    users = []
    for user_obj in user_table:
        usr = user_obj.__dict__
        users.append(usr)
    return users


def get(user_id: int) -> t.Optional[UserRead]:
    usr = None
    usr = db.query(User_db).filter_by(id=user_id).first()
    return usr.__dict__


def create(user_in: UserCreate) -> t.Optional[User]:
    new_user = user_in.dict(exclude_unset=True)

    db.add(User_db(**new_user))
    db.commit()

    return new_user


def update(user_id: int, user_in: UserUpdate) -> t.Optional[User]:
    user_in = user_in.dict(exclude_unset=True)

    user_query = db.query(User_db).filter_by(id=user_id)
    db_user = user_query.first()

    user_query.filter_by(id=user_id).update(user_in, synchronize_session=False)

    db.commit()
    db.refresh(db_user)

    return db_user.__dict__


def delete(user_id: int) -> None:
    # Delete User By Id.
    for index, user in enumerate(user_table):
        if user["id"] == user_id:
            user_table.pop(index)
