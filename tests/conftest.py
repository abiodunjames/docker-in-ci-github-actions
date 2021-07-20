from typing import Iterator

import pytest
from fastapi.testclient import TestClient
from app.api.db import Links, database, engine, metadata
from app.main import app


@pytest.fixture(scope="session", autouse=True)
def client() -> Iterator[TestClient]:
    client = TestClient(app)
    yield client

    metadata.drop_all(engine, checkfirst=True)


@pytest.fixture()
@pytest.mark.asyncio
async def link() -> None:
    query = Links.insert()
    values = {
        "id": "12345",
        "short_url": "https://localhost:8000/12345",
        "original_url": "https://go.me",
        "hit": 0,
    }
    await database.execute(query=query, values=values)
    yield None

    delete_query = Links.delete().where(Links.c.id == "12345")

    await database.execute(query=delete_query)
