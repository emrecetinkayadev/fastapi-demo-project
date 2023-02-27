import datetime

from src.blog.models import PrimaryKey, BlogBase
import typing as t

Post = dict


class PostBase(BlogBase):
    user_id: t.Optional[int]
    title: t.Optional[str]
    content: t.Optional[str]


class PostCreate(PostBase):
    pass


class PostUpdate(BlogBase):
    title: t.Optional[str]
    content: t.Optional[str]


class PostRead(PostBase):
    id: PrimaryKey
