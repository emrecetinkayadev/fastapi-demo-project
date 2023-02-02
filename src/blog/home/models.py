from pydantic import BaseModel


class HomeRead(BaseModel):
    content: str = "Hello World!"
