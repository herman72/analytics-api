from fastapi import APIRouter
from .schemas import EventSchema

router = APIRouter()

@router.get("/")
def read_events():
    return {"results": [1, 2, 3]}


@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    return {"id": event_id}