import pytest

from fastapi_template.handlers.logs import get_all_logs, insert_log
from fastapi_template.models.base import Log
from fastapi_template.schemas.logs import CreateLogRequest
from tests.unit.conftest import MockScalarResult


@pytest.mark.asyncio
async def test_create_log(mock_db):
    await insert_log(db=mock_db, request=CreateLogRequest(info="test log"))

    assert type(mock_db.add.call_args_list[0][0][0]) == Log

    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()


@pytest.mark.asyncio
async def test_get_logs(mock_db):
    async def mock_get_logs_from_db(*args, **kwargs):
        return MockScalarResult([Log(id=1, info="test log")])

    mock_db.scalars = mock_get_logs_from_db

    result = await get_all_logs(mock_db)
    assert type(result[0]) == Log
