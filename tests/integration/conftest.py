import pytest_asyncio
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from fastapi_template.dependencies.db import db
from fastapi_template.main import app
from fastapi_template.models.base import Base

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///test.db"

async_engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

AsyncTestingSessionLocal = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=async_engine,
    class_=AsyncSession,
)


async def override_db():
    db = AsyncTestingSessionLocal()
    try:
        yield db
    finally:
        await db.close()


app.dependency_overrides[db] = override_db


@pytest_asyncio.fixture(scope="session", autouse=True)
async def init_db():
    async with async_engine.begin() as conn:
        print("DROPPING TABLES")
        await conn.run_sync(Base.metadata.drop_all)
        print("CREATING TABLES")
        await conn.run_sync(Base.metadata.create_all)
    yield


client = TestClient(app)
