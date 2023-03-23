from blog.models import BlogBase, PrimaryKey
import typing as t
from pydantic import EmailStr, validator
from .validation import hash_password
from sqlalchemy import TIMESTAMP, Column, String, text, Integer
from blog.db.database import Base

User = dict


class UserBase(BlogBase):
    username: t.Optional[str]
    email: t.Optional[EmailStr]


class UserCreate(UserBase):
    password: t.Optional[str]

    @validator('password')
    def password_hasher(cls, v):
        if type(v) is not str:
            raise ValueError('Password is not string.')
        elif ' ' == v:
            raise ValueError('Password can not be empty.')
        hashed_pass = hash_password(password=v)
        return hashed_pass


class UserUpdate(UserBase):
    password: t.Optional[str]

    @validator('password')
    def password_hasher(cls, v):
        if type(v) is not str:
            raise ValueError('Password is not string.')
        elif ' ' == v:
            raise ValueError('Password can not be empty.')
        hashed_pass = hash_password(password=v)
        return hashed_pass


class UserRead(UserBase):
    id: PrimaryKey = None


class User_db(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String,  nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
