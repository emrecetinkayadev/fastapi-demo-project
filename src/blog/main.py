from fastapi import FastAPI
from blog.home.views import router as home_router
from blog.posts.service import router as post_router

app = FastAPI(
    title="FastAPI Demo",
    description="Welcome to FastAPI Demo documentation!",
    root_path="/",
    docs_url='/docs',
    openapi_url="/docs/openapi.json",
    redoc_url="/redoc"
)

app.include_router(home_router, prefix="/home")
app.include_router(post_router, prefix="/posts")
