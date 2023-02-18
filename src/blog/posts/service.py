from blog.db.db import post_table
from blog.posts.models import PostCreate, PostUpdate, Post
import typing as t

from blog.utils import max_id


def get_all() -> t.List[t.Optional[Post]]:
    return post_table


def get_posts_by_user_id(user_id: int) -> t.List[t.Optional[Post]]:
    user_posts = [post for post in post_table if post["user_id"] == user_id]
    return user_posts


def get(post_id: int) -> t.Optional[Post]:
    searched_post = None
    for post in post_table:
        if post["id"] == post_id:
            searched_post = post

    return searched_post


def create(post_in: PostCreate) -> t.Optional[Post]:
    new_post_id = max_id(post_table) + 1
    new_post = post_in.dict(exclude_unset=True)
    new_post["id"] = new_post_id
    post_table.append(new_post)
    return new_post
    # generate new post ID (use max_id from blog.utils and increment it)
    # Optional: check that user for post exists in user_table by user_id
    # Make 'Post' dict from PostCreate (Post is our alternative to ORM model)
    # add Post to posts_table
    # Return full Post


# Read spec about FastAPI Update approach (currently instead of ORm we use dicts)
# https://sqlmodel.tiangolo.com/tutorial/fastapi/update/
def update(get_post: Post, update_data: PostUpdate) -> Post:
    # post_db later for ORM model we need to get dict from model post_db.dict()
    # update data may contain not all fields from the model
    update_data = update_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        get_post[key] = value

    # When using ORM we will need to commit the changes so that changes to ORM model post_db are reflected in DB
    # For now post_db is in post_table list which contains reference to post_db object, so changes
    # will be reflected automatically

    return get_post


def delete(post_id: int) -> None:
    for index, post in enumerate(post_table):
        if post["id"] == post_id:
            post_table.pop(index)
    # Get user by user_id
    # Delete post id from user's posts list
    # Delete post from post_table
