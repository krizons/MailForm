from fastapi import APIRouter
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


