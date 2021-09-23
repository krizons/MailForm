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

snd = Sender()


@app.on_event("startup")
async def startup():
    snd.obj_task = asyncio.create_task(snd.sender())


@app.on_event("shutdown")
async def shutdown():
    await snd.close()
    await asyncio.wait({snd.obj_task}, return_when=asyncio.FIRST_COMPLETED)
