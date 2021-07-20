import os

from databases import Database
from sqlalchemy import (ARRAY, Column, DateTime, Integer, MetaData, String,
                        Table, create_engine)

from app.api.config import get_settings

settings = get_settings()

DATABASE_URI = settings.DATABASE_URI

engine = create_engine(DATABASE_URI)
metadata = MetaData()

Links = Table(
    "links",
    metadata,
    Column("id", String, primary_key=True),
    Column("short_url", String(40)),
    Column("original_url", String(250)),
    Column("hit", Integer(), default=0),
)

database = Database(DATABASE_URI)
