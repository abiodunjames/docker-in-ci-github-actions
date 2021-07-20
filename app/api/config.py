from functools import lru_cache
from os import environ
from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URI: str = environ.get('DATABASE_URI','')
    DOMAIN_NAME: str = environ.get('DOMAIN_NAME','')


@lru_cache()
def get_settings() -> Settings:
    return Settings()
