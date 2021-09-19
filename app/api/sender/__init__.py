from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from . import (
    all,
    create,
)

router = APIRouter()

router.include_router(
    all.router,
    prefix="/all"
)

router.include_router(
    create.router,
    prefix="/create"
)


@router.get("/",
            response_class=HTMLResponse,
            summary="Форма для взаимодействия с пользователем",
            response_description="Результат запроса получениея формы")
async def get_form():
    return """
    <!DOCTYPE html>
    <html>
    <body>
    <form action="/sender/create/" method="post" enctype="multipart/form-data">
      <label for="heading">Заголовок</label><br>
      <input type="text" id="heading" name="heading" value=""><br>
      <label for="subtitle">Под заголовок:</label><br>
      <input type="text" id="subtitle" name="subtitle" value=""><br>
      <label for="description">Описание:</label><br>
      <textarea rows="10" cols="45" type="text" id="description" name="description" value=""></textarea><br>
      <input name="doc" type="file" multiple><br>
      <input type="submit" value="Submit">
    </form>         
    </body>
    </html>
     """
