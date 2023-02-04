from pydantic import BaseModel


class PostModel(BaseModel):
    user_id: dict
