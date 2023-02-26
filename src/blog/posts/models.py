import datetime

from src.blog.models import PrimaryKey, BlogBase
import typing as t

Post = dict


class PostBase(BlogBase):
    user_id: t.Optional[int]
    created_at: t.Optional[datetime.date]
    title: t.Optional[str]
    content: t.Optional[str]


class PostCreate(PostBase):
    pass


class PostUpdate(BlogBase):
    created_at: t.Optional[datetime.date]
    title: t.Optional[str]
    content: t.Optional[str]


class PostRead(PostBase):
    id: PrimaryKey
