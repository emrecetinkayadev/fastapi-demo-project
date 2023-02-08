import datetime

from blog.models import PrimaryKey, BlogBase
import typing as t

# SQLAlchemy models

# In future this will be an ORM sqlalchemy model,
# For now db objects are simple dict
Post = dict


# Pydantic models
class PostBase(BlogBase):
    user_id: t.Optional[int]
    created_at: t.Optional[datetime.date]
    title: t.Optional[str]
    content: t.Optional[str]


class PostCreate(PostBase):
    id: PrimaryKey = None


class PostUpdate(PostBase):
    id: PrimaryKey = None


class PostRead(PostBase):
    id: PrimaryKey
