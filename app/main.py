from fastapi import FastAPI

from app.api.db import database, engine, metadata
from app.api.routes import route
from fastapi.middleware.cors import CORSMiddleware

metadata.create_all(engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup() -> None:
    await database.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await database.disconnect()


app.include_router(route)
