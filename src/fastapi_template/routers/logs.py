from typing import Sequence

from fastapi import APIRouter, Depends
from fastapi.responses import ORJSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_template.dependencies.db import db
from fastapi_template.handlers.logs import get_all_logs, insert_log
from fastapi_template.schemas.logs import CreateLogRequest, LogSchema

router = APIRouter(prefix="/logs", tags=["logs"])


@router.get("/", response_model=Sequence[LogSchema], response_class=ORJSONResponse)
async def get_logs(db: AsyncSession = Depends(db)):
    return await get_all_logs(db)


@router.post("/", response_model=LogSchema)
async def create_log(request: CreateLogRequest, db: AsyncSession = Depends(db)):
    return await insert_log(request, db)
