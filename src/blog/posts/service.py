from src.blog.posts.models import PostCreate, PostUpdate, Post
import typing as t
from src.blog.db.database import db
from src.blog.db.db_models import Post as Post_db


def get_all() -> t.List[t.Optional[Post]]:
    post_table = list(map(lambda post: post.__dict__, db.query(Post_db).all()))
    return post_table


def get_posts_by_user_id(user_id: int) -> t.List[t.Optional[Post]]:
    posts = list(map(lambda x: x.__dict__, db.query(Post_db).filter(Post_db.user_id == user_id).all()))
    return posts


def get(post_id: int) -> t.Optional[Post]:
    post = db.query(Post_db).filter(Post_db.id == post_id).first()
    if not post:
        return None
    return post.__dict__


def create(post_in: PostCreate) -> t.Optional[Post]:
    post_in_dict = post_in.dict(exclude_unset=True)
    post = Post_db(**post_in_dict)

    db.add(post)
    db.commit()
    db.refresh(post)

    return post.__dict__


def update(post_id: int, update_data: PostUpdate) -> Post:
    update_data_dict = update_data.dict(exclude_unset=True)

    post_query = db.query(Post_db).filter(Post_db.id == post_id)
    post = post_query.first()

    post_query.filter(Post_db.id == post_id).update(update_data_dict, synchronize_session=False)

    db.commit()
    db.refresh(post)

    return post.__dict__


def delete(post_id: int) -> None:
    db.query(Post_db).filter(Post_db.id == post_id).delete(synchronize_session=False)
    db.commit()
