from fastapi import APIRouter
from blog.db.db import db_dict
from blog.posts.models import PostModel

router = APIRouter()


@router.get("", response_model=PostModel)
def get_posts():
    """Get all posts in DB.
    """
    return PostModel(user_id=db_dict)
