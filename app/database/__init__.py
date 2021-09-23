from functools import lru_cache
from sqlalchemy import create_engine
from .db_model import mail_task
from conf import settings
from sqlalchemy.ext.asyncio import create_async_engine


@lru_cache()
def get_db_engine():
    return create_async_engine(
        settings.DATABASE_URL,
        pool_size=settings.DB_POOL_SIZE,
        max_overflow=0,
        connect_args={
            "server_settings": {
                "application_name": "2fa",
                "client_encoding": "utf-8",
                "timezone": "utc"
            }
        }
    )


db = get_db_engine()
