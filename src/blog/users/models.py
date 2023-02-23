from blog.models import BlogBase, PrimaryKey
import typing as t
from pydantic import EmailStr, validator
from .validation import hash_password

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
