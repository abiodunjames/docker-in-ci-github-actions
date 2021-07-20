from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder

from app.api.models import Url, UrlInput, UrlOutput
from app.api.service import create_link, get_link, list_link
from typing import List

route = APIRouter()


@route.get("/api/health")
async def index():
    return {"live": "true"}


@route.post("/api/urls", response_model=UrlOutput)
async def create_short_link(request: UrlInput) -> UrlOutput:
    url = await create_link(request)
    return url


@route.get("/api/urls", response_model=List[Url])
async def list_all_links() -> List[Url]:
    urls = await list_link()
    return urls


@route.get("/api/health")
async def index():
    return {"live": "true"}


@route.get("/{id}", response_model=UrlOutput)
async def get_short_link(id: str) -> UrlOutput:
    url = await get_link(id)
    if url != None:
        return url
    raise HTTPException(status_code=404)
