from sqlalchemy.exc import DatabaseError, SQLAlchemyError, TimeoutError
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from fastapi_template.settings.environment import get_settings

engine = create_async_engine(get_settings().DB_URL)
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)


class AsyncDatabaseSession:
    async def __call__(self):
        async_session = SessionLocal()
        try:
            yield async_session
        except (TimeoutError, DatabaseError, SQLAlchemyError):
            await async_session.rollback()
        finally:
            await async_session.close()


db = AsyncDatabaseSession()
