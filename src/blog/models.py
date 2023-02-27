# pydantic type that limits the range of primary keys
from pydantic import BaseModel
from pydantic.types import conint

# Create custom type for id
PrimaryKey = conint(gt=0, lt=2147483647)


# Pydantic models...
class BlogBase(BaseModel):
    class Config:
        orm_mode = True
        validate_assignment = True
        arbitrary_types_allowed = True
