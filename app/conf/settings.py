from pydantic import BaseSettings


class Settings(BaseSettings):
    SEND_MAIL: str
    DATABASE_URL: str
    SMTP_HOST: str
    SMTP_PORT: int
    FROM_MAIL: str
    FILE_SAVE_PATH: str
    LOGIN: str
    PASS: str
    SMTP_LOGIN: str
    SMTP_PASS: str
    class Config:
        env_file = "../.env"
