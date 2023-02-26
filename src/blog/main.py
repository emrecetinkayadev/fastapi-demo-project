from fastapi import FastAPI
from src.blog.home.views import router as home_router
from src.blog.posts.views import router as post_router
from src.blog.users.views import router as user_router
from src.blog.db.database import create_tables

app = FastAPI(
    title="FastAPI Demo",
    description="Welcome to FastAPI Demo documentation!",
    root_path="/",
    docs_url='/docs',
    openapi_url="/docs/openapi.json",
    redoc_url="/redoc"
)


@app.on_event("startup")
def startup_event():
    create_tables()


app.include_router(home_router, prefix="/home", tags=["home"])
app.include_router(post_router, prefix="/posts", tags=["posts"])
app.include_router(user_router, prefix="/users", tags=["users"])
