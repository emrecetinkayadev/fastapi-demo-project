from fastapi import APIRouter, HTTPException, status
from .models import PostCreate, PostUpdate, PostRead
from .service import get, create, get_all, delete, update
import typing as t
from blog.models import PrimaryKey

router = APIRouter()


@router.get("", response_model=t.List[PostRead])
def get_posts():
    """
    Get all posts.
    """
    return get_all()


@router.get("/{post_id}", response_model=PostRead)
def get_post(post_id: PrimaryKey):
    """Get post by ID."""
    post = get(post_id=post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "Post with this id doesn't exist"}]
        )

    return post


@router.post("", response_model=PostRead)
def create_post(post_in: PostCreate):
    """Create a new post."""
    # call service method create
    post = create(post_in)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=[{"msg": "Error happened when trying to creating post."}],
        )
    return post


@router.put("/{post_id}", response_model=PostRead)
def update_post(post_id: PrimaryKey, post_in: PostUpdate):
    """Update a post by ID."""
    post = get(post_id=post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "Post with this id doesn't exist"}],
        )

    updated_post = update(get_post=post, update_data=post_in)
    return updated_post


@router.delete("/{post_id}", response_model=None)
def delete_post(post_id: PrimaryKey):
    """Delete a post by ID."""
    post = get(post_id=post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "Post with this id doesn't exist"}],
        )
    delete(post_id=post_id)
    # get post by id using service method
    # if not post raise 404 HTTPException (check specification: https://fastapi.tiangolo.com/tutorial/handling-errors/ )
    # else post exists, call delete from service
    # usually no need to return anything from delete, sometimes the deleted id can be returned,
    # but it's ok to return just HTTP 200 response
    # (If there are no exceptions raised and no return, FastAPI automatically return HTTP 200)
