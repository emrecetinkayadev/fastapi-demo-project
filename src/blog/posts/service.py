from blog.posts.models import PostCreate, PostUpdate, Post, PostDB
import typing as t
from sqlalchemy.orm import Session


def get_all(db: Session) -> t.List[t.Optional[Post]]:
    post_table = db.query(PostDB).all()
    return post_table


def get_posts_by_user_id(db: Session, user_id: int) -> t.List[t.Optional[Post]]:
    posts = db.query(PostDB).filter(PostDB.user_id == user_id).all()
    return posts


def get(db: Session, post_id: int) -> t.Optional[Post]:
    post = db.query(PostDB).filter(PostDB.id == post_id).first()
    if not post:
        return None
    return post


def create(db: Session, post_in: PostCreate) -> t.Optional[Post]:
    post_in_dict = post_in.dict(exclude_unset=True)
    post = PostDB(**post_in_dict)

    db.add(post)
    db.commit()
    db.refresh(post)

    return post


def update(db: Session, post_id: int, update_data: PostUpdate) -> Post:
    update_data_dict = update_data.dict(exclude_unset=True)

    post_query = db.query(PostDB).filter(PostDB.id == post_id)
    post = post_query.first()

    post_query.filter(PostDB.id == post_id).update(update_data_dict, synchronize_session=False)

    db.commit()
    db.refresh(post)

    return post


def delete(db: Session, post_id: int) -> None:
    db.query(PostDB).filter(PostDB.id == post_id).delete(synchronize_session=False)
    db.commit()
