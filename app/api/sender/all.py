from fastapi import APIRouter, Depends
from .model import *
from database import (
    db,
    mail_task,
)
from depends import (
    HTTPBasicCredentials,
    get_current_username,
    security
)
from depends import (
    HTTPBasicCredentials,
    get_current_username,
    security
)

router = APIRouter()


@router.get("/",
            summary="Запрос на получение всех категорий или подкатегорий выбраной категории",
            response_model=list,
            response_description="Результат запроса на получение всех категорий или подкатегорий выбраной категории")
async def all_category(credentials: HTTPBasicCredentials = Depends(security)):
    get_current_username(credentials)
    qu = mail_task.select()
    row = await db.fetch_all(qu)
    data_response = []
    for el in row:
        data_response.append(
            AllTaskResponse(heading=el.get("heading"), id=el.get("id"), subtitle=el.get("subtitle"),
                            description=el.get("description")))
    return data_response
