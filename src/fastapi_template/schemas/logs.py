from typing import Optional

from pydantic import BaseModel


class CreateLogRequest(BaseModel):
    info: str


class LogSchema(BaseModel):
    id: int
    info: Optional[str]
