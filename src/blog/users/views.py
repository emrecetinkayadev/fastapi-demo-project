from fastapi import APIRouter, HTTPException, status, Depends
from .models import UserCreate, UserRead, UserUpdate
from .service import get_all, get, create, delete, update, check_email
from src.blog.posts.service import get_posts_by_user_id
from sqlalchemy.orm import Session
import typing as t
from src.blog.models import PrimaryKey
from src.blog.db.database import get_db

router = APIRouter()


@router.get("", response_model=t.List[UserRead])
def get_users(db: Session = Depends(get_db)):
    """
    Get all Users.
    """
    return get_all(db=db)


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: PrimaryKey, db: Session = Depends(get_db)):
    """
    Get User by ID.
    """

    user = get(user_id=user_id, db=db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "User with this ID doesn't exist"}]
        )
    return user


@router.post("", response_model=UserRead)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    """Create new user.

    Args:
        user_in (UserCreate): User json object.
    """
    check = check_email(user_in.email, db=db)
    if check:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=[{"msg": "The user with this email address already exists."}]
        )
    user = create(user_in, db=db)
    return user


@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: PrimaryKey, user_in: UserUpdate, db: Session = Depends(get_db)):
    """Update User by ID.

    Args:
        user_id (PrimaryKey): user id
        user_in (UserUpdate): user data

    Raises:
        HTTPException: if user not found.

    Returns:
        _type_: User Data.
    """
    user = get(user_id=user_id, db=db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "User with this ID doesn't exist"}]
        )

    user_in = update(user_id=user_id, update_data=user_in, db=db)
    return user_in


@router.delete("/{user_id}", response_model=None)
def delete_user(user_id: PrimaryKey, db: Session = Depends(get_db)):
    """ Delete User by ID.

    Args:
        user_id (PrimaryKey): Integer ID value
    """
    user = get(user_id=user_id, db=db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "User with this ID doesn't exist"}]
        )
    delete(user_id=user_id, db=db)
