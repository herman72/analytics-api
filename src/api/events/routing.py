from fastapi import APIRouter
from .schemas import (EventSchema, 
                      EventListSchema, 
                      EventCreateSchema, 
                      EventUpdateSchema
                      )

router = APIRouter()

# List view /api/events
@router.get("/")
def read_events() -> EventListSchema:
    return {
        "results": [
            {"id":1}, {"id":2}, {"id":3}
                    ],
        "count": 3
        }


@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    return {"id": event_id}

# Send Data here
# post view
# Post /api/events
@router.post("/")
def create_events(payload: EventCreateSchema) -> EventSchema:
    print(payload)
    data = payload.model_dump()
    return {"id": 123, **data}

# update data
# PUT /api/events/12
@router.put("/{event_id}")
def update_event(event_id: int, payload: EventUpdateSchema) -> EventSchema:
    print(payload)
    data = payload.model_dump()
    return {"id": event_id, **data}

#Delete
# @router.delete("/{event_id}")
# def get_event(event_id: int) -> EventSchema:
#     return {"id": event_id}
