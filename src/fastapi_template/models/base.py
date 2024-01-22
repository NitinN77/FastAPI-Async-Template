from typing import Any, Optional

from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Log(Base):
    __tablename__ = "logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    info: Mapped[str] = mapped_column(String, nullable=True)

    def __init__(self, info: Optional[str]):
        self.info = info
