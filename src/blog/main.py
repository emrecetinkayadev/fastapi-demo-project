from fastapi import FastAPI
from blog.home.views import router as home_router
from blog.posts.views import router as post_router
from blog.users.views import router as user_router

app = FastAPI(
    title="FastAPI Demo",
    description="Welcome to FastAPI Demo documentation!",
    root_path="/",
    docs_url='/docs',
    openapi_url="/docs/openapi.json",
    redoc_url="/redoc"
)

app.include_router(home_router, prefix="/home", tags=["home"])
app.include_router(post_router, prefix="/posts", tags=["posts"])
app.include_router(user_router, prefix="/users", tags=["users"])
