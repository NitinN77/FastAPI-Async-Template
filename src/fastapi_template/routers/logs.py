from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_template.dependencies import db
from fastapi_template.handlers.logs import get_all_logs, insert_log
from fastapi_template.schemas.logs import CreateLogRequest

router = APIRouter(prefix="/logs", tags=["logs"])


@router.get("/")
async def get_logs(db: AsyncSession = Depends(db)):
    return await get_all_logs(db)


@router.post("/")
async def create_log(request: CreateLogRequest, db: AsyncSession = Depends(db)):
    return await insert_log(request, db)
