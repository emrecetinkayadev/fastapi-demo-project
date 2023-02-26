from fastapi import APIRouter

from src.blog.home.models import HomeRead

router = APIRouter()


@router.get("", response_model=HomeRead)
def get_definitions():
    """Get all definitions."""
    return HomeRead(content="This is Fast API demo project")
