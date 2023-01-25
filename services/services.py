from fastapi.routing import APIRouter
import aiohttp
from fastapi import FastAPI

app = FastAPI()
router = APIRouter()

@router.get("/hello")
def hello():
    return {"hello": "World"}


@router.get("/random-word")
async def random_word():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://random-word-api.herokuapp.com/word") as resp:
            data = await resp.json()
            if data:
                return data
            else:
                return None


app.include_router(router, prefix="/v1")