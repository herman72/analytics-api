from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from api.db.session import get_session
from .models import (EventModel, 
                      EventBucketSchema, 
                      EventCreateSchema, 
                      get_utc_now
                      )
from timescaledb.hyperfunctions import time_bucket
from sqlalchemy import case, func

from datetime import datetime, timedelta, timezone
# from api.db.config import DATABASE_URL

router = APIRouter()
DEFAULT_LOOKUP_PAGES = [
        "/", "/about", "/pricing", "/contact", 
        "/blog", "/products", "/login", "/signup",
        "/dashboard", "/settings"
    ]
# List view /api/events
@router.get("/", response_model=List[EventBucketSchema])
def read_events(
    duration: str = Query(default="1 day"),
    pages: List = Query(default=None),
    session: Session=Depends(get_session)
    ):
    # a bunch of items in a table
    os_case = case(
        (EventModel.user_agent.ilike('%windows%'), 'Windows'),
        (EventModel.user_agent.ilike('%macintosh%'), 'MacOS'),
        (EventModel.user_agent.ilike('%iphone%'), 'iOS'),
        (EventModel.user_agent.ilike('%android%'), 'Android'),
        (EventModel.user_agent.ilike('%linux%'), 'Linux'),
        else_='Other'
    ).label('operating_system')
    # print(os.environ.get("DATABASE_URL"), DATABASE_URL)
    bucket = time_bucket(duration, EventModel.time)
    lookup_pages = pages if isinstance(pages, list) and len(pages) > 0 else DEFAULT_LOOKUP_PAGES
    query = (
        select(
            bucket.label("bucket"),
            os_case,
            EventModel.page.label("page"),
            func.avg(EventModel.duration).label("avg_duration"),
            func.count().label("count")
        )
        .where(
            EventModel.page.in_(lookup_pages)
        )
        .group_by(
            bucket,
            os_case,
            EventModel.page,
        )
        .order_by(
            bucket,
            os_case,
            EventModel.page,
        )
    )
    results = session.exec(query).fetchall( )
    return results



# @router.get("/", response_model=EventListSchema)
# def read_events(session: Session=Depends(get_session)):
#     # print(os.environ.get("DATABASE_URL"), DATABASE_URL)
#     query = select(EventModel).order_by(EventModel.id.desc()).limit(10)
#     results = session.exec(query).all( )
#     return {
#         "results": results,
#         "count": len(results)
#         }



# Send Data here
# post view
# Post /api/events
@router.post("/", response_model=EventModel)
def create_events(payload: EventCreateSchema,
                  session: Session=Depends(get_session)):
    print(payload)
    data = payload.model_dump()
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj


@router.get("/{event_id}", response_model=EventModel)
def get_event(event_id: int,
              session: Session=Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    resutl = session.exec(query).first()
    if not resutl:
        raise HTTPException(status_code=404, detail="Event not found")
    return resutl


# update data
# PUT /api/events/12
# @router.put("/{event_id}", response_model=EventModel)
# def update_event(event_id: int, 
#                  payload: EventUpdateSchema, 
#                  session: Session=Depends(get_session)):
#     query = select(EventModel).where(EventModel.id == event_id)
#     obj = session.exec(query).first()
#     if not obj:
#         raise HTTPException(status_code=404, detail="Event not found")
#     data = payload.model_dump()
#     print(type(data))
#     for k, v in data.items():
#         setattr(obj, k, v)
#     obj.updated_at = get_utc_now()
#     session.add(obj)
#     session.commit()
#     session.refresh(obj)
#     return obj

#Delete
# @router.delete("/{event_id}")
# def get_event(event_id: int) -> EventSchema:
#     return {"id": event_id}
