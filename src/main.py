from typing import Union
from fastapi import FastAPI
from api.events import router as events_router
from api.db.session import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    return

app = FastAPI(lifespan=lifespan)
app.include_router(events_router, prefix="/api/events")


@app.get("/")
def read_root():
    return {"hello": "world"}

@app.get("/item/{item_id}")
def read_item(item_id: int, q: Union[str, None]=None):
    return {"item_id": item_id, "q":q}

@app.get("/healthz")
def read_api_health():
    return {"status": "ok"}