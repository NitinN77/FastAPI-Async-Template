from typing import Any
from unittest.mock import AsyncMock, MagicMock

import pytest


@pytest.fixture()
def mock_db():
    mock_db = MagicMock()
    mock_db.commit = AsyncMock()
    mock_db.refresh = AsyncMock()
    return mock_db


class MockScalarResult:
    def __init__(self, result: list[Any]) -> None:
        self.result = result

    def all(self):
        return self.result
