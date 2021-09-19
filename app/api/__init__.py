from fastapi import APIRouter
from . import sender


router = APIRouter()

router.include_router(
    sender.router,
    prefix="/sender"
)



