from app.api.db import Links, database
from app.api.models import Url, UrlInput, UrlOutput


async def create(payload: Url) -> int:
    query = Links.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get(id: str) -> Links:
    query = Links.select(Links.c.id == id)
    return await database.fetch_one(query=query)

async def list_all():
    query = Links.select()
    return await database.fetch_all(query=query)

async def update_link_hit(link: Links, hit: int) -> None:
    """ Update hit attribute of a link.
    Args:
        link (Link): Link to update.
        hit  (int): New value
    """
    query = Links.update().values({"hit": hit})
    await database.execute(query=query)


async def link_exists(key: str) -> bool:
    """ Check if the given key exists in the database.
    Args:
        key (str): The key to check.

    Returns:
        bool: The return value. True for success, False otherwise.
    """
    result = await get(key)
    if result == None:
        return False
    return True
