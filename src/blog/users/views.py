from fastapi import APIRouter, HTTPException, status
from .models import UserCreate, UserRead
from .service import get_all, get, create

import typing as t
from blog.models import PrimaryKey

router = APIRouter()


@router.get("", response_model=t.List[UserRead])
def get_users():
    """
    Get all Users.
    """
    return get_all()


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: PrimaryKey):
    """
    Get User by ID.
    """
    user = get(user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "User with this ID doesn't exist"}]
        )
    return user


@router.post("", response_model=UserRead)
def create_user(user_in: UserCreate):
    """Create new user.

    Args:
        user_in (UserCreate): User json object.
    """
    user = create(user_in)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=[{"msg": "Error happened when trying to user creation"}]
        )
    return user
