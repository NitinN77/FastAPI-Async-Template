from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_template.dependencies import db
from fastapi_template.models import Log
from fastapi_template.schemas.logs import CreateLogRequest

router = APIRouter(prefix="/logs", tags=["logs"])


@router.get("/")
async def get_logs(db: AsyncSession = Depends(db)):
    logs = await db.scalars(select(Log))
    return logs.all()


@router.post("/")
async def create_log(request: CreateLogRequest, db: AsyncSession = Depends(db)):
    new_log = Log(request.info)

    db.add(new_log)
    await db.commit()
    await db.refresh(new_log)

    return new_log
