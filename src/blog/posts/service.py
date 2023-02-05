from fastapi import APIRouter
from blog.db.db import db_dict
from blog.posts.models import PostModel
import uuid

router = APIRouter()


@router.get("", response_model=dict)
def get_posts():
    """Get all posts in DB.
    """
    return db_dict


@router.post("", response_model=str)
def create_post(post: PostModel):
    """create a new post.
    """
    unique_id = str(uuid.uuid4())
    if post.user_id in db_dict:
        db_dict[post.user_id][unique_id] = post.content
    else:
        db_dict[post.user_id] = {}
        db_dict[post.user_id][unique_id] = post.content
    return f"{post.user_id} : {post.content} - 201 new post."
