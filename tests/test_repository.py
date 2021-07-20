import pytest

from app.api.db import Links, database
from app.api.models import Url
from app.api.repository import create, get, link_exists, update_link_hit


@pytest.mark.asyncio
async def test_create() -> None:
    url = Url(
        id="absTy461",
        short_url="http://tier.app/absTy461",
        original_url="https://fb.com",
        hit=0,
    )
    response = await create(url)
    assert response == 1


@pytest.mark.asyncio
async def test_get(link: None) -> None:
    response = await get("12345")
    assert response.id == "12345"
    assert response.short_url == "https://localhost:8000/12345"
    assert response.hit == 0


@pytest.mark.asyncio
async def test_update_link_hit(link: None) -> None:
    link = await get("12345")
    await update_link_hit(link, 4)
    updated_link = await get("12345")
    assert updated_link.hit == 4


@pytest.mark.asyncio
async def test_update_link_hit(link: None) -> None:
    assert await link_exists("12345")
