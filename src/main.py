from fastapi import FastAPI
from contextlib import asynccontextmanager

from .db import db_init
from .routers.user import user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_init()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(user_router)