from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # used by the FastAPI application, uses asyncpg
    DB_URL: Optional[str] = None

    # used by alembic to apply migrations, uses psycopg2
    DB_URL_FOR_MIGRATIONS: Optional[str] = None

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings():
    return Settings()
