from blog.models import PrimaryKey, BlogBase
import typing as t
from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, text, Integer, DateTime
from sqlalchemy.orm import relationship
from blog.db.database import Base
from datetime import datetime


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


class PostDB(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    user = relationship('UserDB')
