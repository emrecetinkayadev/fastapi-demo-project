from fastapi import FastAPI
import aiohttp

app = FastAPI()


@app.get("/hello")
def hello():
    return {"hello": "World"}


@app.get("/random-word")
async def random_word():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://random-word-api.herokuapp.com/word") as resp:
            data = await resp.json()
            if data:
                return data
            else:
                return None
