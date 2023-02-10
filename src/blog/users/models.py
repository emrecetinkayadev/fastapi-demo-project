from blog.models import BlogBase, PrimaryKey
import typing as t
from pydantic import EmailStr

User = dict


class UserBase(BlogBase):
    username: t.Optional[str]
    email: t.Optional[EmailStr]


class UserCreate(UserBase):
    password: t.Optional[str]


class UserRead(UserBase):
    id: PrimaryKey = None
