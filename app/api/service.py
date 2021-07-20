import re
from secrets import token_urlsafe
from typing import Optional, List

from sqlalchemy.engine.result import RowProxy

from app.api import repository
from app.api.config import get_settings
from app.api.db import Links
from app.api.models import Url, UrlInput, UrlOutput

settings = get_settings()


async def create_link(payload: UrlInput) -> Url:
    key = await generate_key()
    short_url = f"{settings.DOMAIN_NAME}/{key}"
    new_url: Url = Url(id=key, original_url=payload.url, short_url=short_url)
    await repository.create(new_url)

    return new_url


async def list_link() -> List[Url]:
    return await repository.list_all()


async def get_link(key: str) -> Optional[RowProxy]:
    """Returns a link object and increment the hit by 1.
    Args:
        key (str): The primary key of the link.

    Returns:
        Links : a Link object
        None : If not found
    """
    link: Links = await repository.get(key)
    if link != None:
        hit: int = Links.c.hit + 1
        await repository.update_link_hit(link, hit)
        return link
    return None


async def generate_key() -> str:
    """
    Generate url-safe code
    """
    code = re.sub("-", "", token_urlsafe(8))
    exists = await repository.link_exists(code)
    while exists:
        generate_key()
    return code
