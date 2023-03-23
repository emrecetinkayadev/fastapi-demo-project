from blog.users.models import User, UserCreate, UserUpdate, UserRead, User_db
import typing as t
from sqlalchemy.orm import Session


def get_all(db: Session) -> t.List[t.Optional[UserRead]]:
    user_table = db.query(User_db).all()
    return user_table


def get(user_id: int, db: Session) -> t.Optional[UserRead]:
    user = db.query(User_db).filter(User_db.id == user_id).first()
    if not user:
        return None
    return user


def create(user_in: UserCreate, db: Session) -> t.Optional[User]:
    new_user = user_in.dict(exclude_unset=True)

    db.add(User_db(**new_user))
    db.commit()

    return new_user


def update(user_id: int, update_data: UserUpdate, db: Session) -> t.Optional[User]:
    update_data = update_data.dict(exclude_unset=True)

    user_query = db.query(User_db).filter(User_db.id == user_id)
    user = user_query.first()

    user_query.filter_by(id=user_id).update(update_data, synchronize_session=False)

    db.commit()
    db.refresh(user)

    return user


def delete(user_id: int, db: Session) -> None:
    # Delete User By Id.
    db.query(User_db).filter(User_db.id == user_id).delete(synchronize_session=False)
    db.commit()


def check_email(user_mail, db: Session) -> bool:
    user = db.query(User_db).filter(User_db.email == user_mail).first()
    if not user:
        return False
    return True
