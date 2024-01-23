import pytest

from tests.integration.conftest import client


@pytest.mark.asyncio
async def test_create_log():
    response = client.post("/logs/", json={"info": "test log 1"})
    assert response.status_code == 200
    response_body = response.json()

    assert type(response_body["id"]) == int
    assert response_body["info"] == "test log 1"


@pytest.mark.asyncio
async def test_create_log_with_invalid_info_datatype():
    response = client.post("/logs/", json={"info": 123})
    assert response.status_code == 422
    response_body = response.json()

    assert response_body == {
        "detail": [
            {
                "type": "string_type",
                "loc": ["body", "info"],
                "msg": "Input should be a valid string",
                "input": 123,
                "url": "https://errors.pydantic.dev/2.5/v/string_type",
            }
        ]
    }


@pytest.mark.asyncio
async def test_get_logs():
    response = client.get("/logs")
    assert response.status_code == 200
    response_body = response.json()[0]

    assert type(response_body["id"]) == int
    assert response_body["info"] == "test log 1"
