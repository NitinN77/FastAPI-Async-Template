from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_template.models import Log
from fastapi_template.schemas.logs import CreateLogRequest
from fastapi_template.utils.logger import logger


async def get_all_logs(db: AsyncSession):
    logs = await db.scalars(select(Log))
    return logs.all()


async def insert_log(request: CreateLogRequest, db: AsyncSession):
    new_log = Log(info=request.info)

    db.add(new_log)
    await db.commit()
    await db.refresh(new_log)

    logger.info(f"Inserted log: {request.model_dump()}")
    return new_log
