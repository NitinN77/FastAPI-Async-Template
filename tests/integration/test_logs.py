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
async def test_get_logs():
    response = client.get("/logs")
    assert response.status_code == 200
    response_body = response.json()[0]

    assert type(response_body["id"]) == int
    assert response_body["info"] == "test log 1"
