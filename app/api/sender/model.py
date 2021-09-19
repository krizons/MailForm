from pydantic import BaseModel
from fastapi import Form


class CreateTaskRequest(BaseModel):
    heading: str
    subtitle: str
    description: str

    @classmethod
    def as_form(
            cls,
            heading: str = Form(...),
            subtitle: str = Form(...),
            description: str = Form(...)
    ):

        return cls(heading=heading, subtitle=subtitle, description=description)

    class Config:
        title = "Запрос на создание задания sender"

        fields = dict(
            heading=dict(
                title="Заголовок"
            ),
            subtitle=dict(
                title="Подзаголовок"
            ),
            description=dict(
                title="Описание"
            ),

        )


class CreateTaskResponse(BaseModel):
    status: str
    result: str

    class Config:
        title = "Запрос на создание задания sender"
        fields = dict(
            status=dict(
                title="Статус операции"
            ),
            result=dict(
                title="Сообщение"
            )
        )


class AllTaskResponse(BaseModel):
    heading: str
    subtitle: str
    description: str

    class Config:
        title = "Запрос на создание задания sender"
        fields = dict(
            heading=dict(
                title="Заголовко"
            ),
            subtitle=dict(
                title="Подзаголовок"
            ),
            description=dict(
                title="Описание"
            )
        )
