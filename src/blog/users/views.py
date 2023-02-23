from fastapi import APIRouter, HTTPException, status
from .models import UserCreate, UserRead, UserUpdate
from .service import get_all, get, create, delete, update
from blog.posts.service import get_posts_by_user_id
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


@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: PrimaryKey, user_in: UserUpdate):
    user = get(user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "User with this ID doesn't exist"}]
        )

    user_in = update(user_id=user_id, user_in=user_in)
    return user_in


@router.delete("/{user_id}", response_model=None)
def delete_user(user_id: PrimaryKey):
    """ Delete User by ID.

    Args:
        user_id (PrimaryKey): Integer ID value
    """
    user = get(user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "User with this ID doesn't exist"}]
        )
    delete(user_id=user_id)
