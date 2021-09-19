from fastapi import APIRouter, Depends, File, UploadFile
from .model import *
import sqlalchemy
from conf import settings
import random
import aiofiles
from database import (
    db,
    mail_task
)
from depends import (
    HTTPBasicCredentials,
    get_current_username,
    security
)

router = APIRouter()


@router.post("/",
             summary='Запрос на создание задания',
             response_model=CreateTaskResponse,
             response_description="Результат запроса на создание задания")
async def create_category(req: CreateTaskRequest = Depends(), doc: UploadFile = File(...),
                          credentials: HTTPBasicCredentials = Depends(security)):
    get_current_username(credentials)
    doc_path = settings.FILE_SAVE_PATH + str(random.randint(0, 1000000)) + "_" + doc.filename
    await db.execute(mail_task.insert(), {"heading": req.heading,
                                          "subtitle": req.subtitle,
                                          "description": req.description,
                                          "path_doc": doc_path})
    async with aiofiles.open(doc_path, 'wb') as doc_file_file:
        binfile = await doc.read()
        await doc_file_file.write(binfile)
        return CreateTaskResponse(status="OK", result="")

    #return CreateTaskResponse(status="Fault", result="")
