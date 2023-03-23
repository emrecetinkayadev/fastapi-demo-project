from blog.models import PrimaryKey, BlogBase
import typing as t
from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, text, Integer
from sqlalchemy.orm import relationship
from blog.db.database import Base


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


class Post_db(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    user = relationship('User_db')
