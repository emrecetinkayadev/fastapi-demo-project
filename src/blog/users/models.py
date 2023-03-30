from blog.models import BlogBase, PrimaryKey
import typing as t
from pydantic import EmailStr, validator
from .validation import hash_password
from sqlalchemy import TIMESTAMP, Column, String, text, Integer, DateTime
from blog.db.database import Base
from datetime import datetime

User = dict


class UserBase(BlogBase):
    username: t.Optional[str]
    email: t.Optional[EmailStr]


class UserCreate(UserBase):
    password: t.Optional[str]

    @validator('password', allow_reuse=True)
    def password_hasher(cls, v):
        if type(v) is not str:
            raise ValueError('Password is not string.')
        elif ' ' == v:
            raise ValueError('Password can not be empty.')
        hashed_pass = hash_password(password=v)
        return hashed_pass


class UserUpdate(UserBase):
    password: t.Optional[str]

    @validator('password', allow_reuse=True)
    def password_hasher(cls, v):
        if type(v) is not str:
            raise ValueError('Password is not string.')
        elif ' ' == v:
            raise ValueError('Password can not be empty.')
        hashed_pass = hash_password(password=v)
        return hashed_pass


class UserRead(UserBase):
    id: PrimaryKey = None


class UserDB(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String,  nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
