from pydantic import AnyUrl, BaseModel, ValidationError


class Url(BaseModel):
    id: str
    short_url:  str
    original_url: str
    hit : int = 0

class UrlInput(BaseModel):
    url: AnyUrl


class UrlOutput(BaseModel):
    short_url: AnyUrl
    original_url: AnyUrl
