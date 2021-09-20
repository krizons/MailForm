from fastapi import FastAPI
from database import db
import api
from conf import settings
from sender import Sender
import asyncio

app = FastAPI()

app.include_router(
    api.router
)

Snd = Sender()
asyncio.gather(Snd.sender())


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
    await Snd.close()
