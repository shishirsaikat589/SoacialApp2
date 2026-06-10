from fastapi import FastAPI
from contextlib import asynccontextmanager
import os

from database import engine, Base
from routers import users, posts


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    os.makedirs("static/uploads", exist_ok=True)
    yield


app = FastAPI(title="Social App", lifespan=lifespan)

app.include_router(users.router)
