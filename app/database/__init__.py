from databases import Database
from .db_model import mail_task
from conf import settings

db: Database = Database(settings.DATABASE_URL)
