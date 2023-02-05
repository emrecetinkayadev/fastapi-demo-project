from fastapi import APIRouter
from blog.db.db import db_dict
from blog.posts.models import PostModel
import uuid

router = APIRouter()


@router.get("", response_model=dict)
def get_posts():
    """
    Get all posts in DB.
    """
    return db_dict


@router.post("", response_model=str)
def create_post(post: PostModel):
    """
    create a new post.
    """
    unique_id = str(uuid.uuid4())
    if post.user_id in db_dict:
        db_dict[post.user_id][unique_id] = post.content
    else:
        db_dict[post.user_id] = {}
        db_dict[post.user_id][unique_id] = post.content
    return f"{post.user_id} : {post.content} - 201 new post."


@router.delete("", response_model=str)
def delete_post(post_id: str, body: dict):
    """
    delete a post by ID.
    """
    if post_id in db_dict[body["user_id"]]:
        del db_dict[body["user_id"]][post_id]
        message = f"Post deleted ID: {post_id}"
    else:
        message = "ID not found."
    return message


@router.put("", response_model=str)
def update_post(post: PostModel):
    """
    update a new post.
    """
    if post.user_id in db_dict:
        for key in post.content.keys():
            if key in db_dict[post.user_id]:
                db_dict[post.user_id][key] = post.content[key]
                message = f"{post.user_id} : {post.content} - post updated."
            else:
                message = "POST does not exists."
    return message
