import pytest

from app.api.service import get_link


@pytest.mark.asyncio
async def test_get_link(link: None) -> None:
    """ Test that link has correct hit (number of visits) """
    first_retrieval = await get_link("12345")
    assert first_retrieval.hit == 0
    second_retrieval = await get_link("12345")
    assert second_retrieval.hit == 1


@pytest.mark.asyncio
async def test_get_invalid_link() -> None:
    link = await get_link("non-valid-link")
    assert link == None