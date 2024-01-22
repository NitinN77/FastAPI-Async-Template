from fastapi import APIRouter

from .logs import router as logs_router

main_router = APIRouter()

main_router.include_router(logs_router)
