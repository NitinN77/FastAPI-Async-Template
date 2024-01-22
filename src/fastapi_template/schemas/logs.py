from pydantic import BaseModel


class CreateLogRequest(BaseModel):
    info: str
