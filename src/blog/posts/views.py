from fastapi import APIRouter, HTTPException, status, Depends
from .models import PostCreate, PostUpdate, PostRead
from .service import get, create, get_all, delete, update
import typing as t
from blog.models import PrimaryKey
from blog.db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("", response_model=t.List[PostRead])
def get_posts(db: Session = Depends(get_db)):
    """
    Get all posts.
    """
    return get_all(db=db)


@router.get("/{post_id}", response_model=PostRead)
def get_post(post_id: PrimaryKey, db: Session = Depends(get_db)):
    """Get post by ID."""
    post = get(db=db, post_id=post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "Post with this id doesn't exist"}]
        )

    return post


@router.post("", response_model=PostRead)
def create_post(post_in: PostCreate, db: Session = Depends(get_db)):
    """Create a new post."""
    post = create(post_in=post_in, db=db)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=[{"msg": "Error happened when trying to creating post."}],
        )
    return post


@router.put("/{post_id}", response_model=PostRead)
def update_post(post_id: PrimaryKey, post_in: PostUpdate, db: Session = Depends(get_db)):
    """Update a post by ID."""
    post = get(post_id=post_id, db=db)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "Post with this id doesn't exist"}],
        )

    updated_post = update(post_id=post_id, update_data=post_in, db=db)
    return updated_post


@router.delete("/{post_id}", response_model=None)
def delete_post(post_id: PrimaryKey, db: Session = Depends(get_db)):
    """Delete a post by ID."""
    post = get(post_id=post_id, db=db)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "Post with this id doesn't exist"}],
        )
    delete(post_id=post_id, db=db)
