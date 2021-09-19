from fastapi import FastAPI
from database import db
import api
from  conf import settings
app = FastAPI()

app.include_router(
    api.router
)


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()