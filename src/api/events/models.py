from typing import List, Optional
# from pydantic import BaseModel, Field
from sqlmodel import SQLModel, Field

"""
id
path
description    
"""

class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] = Field(default="")

class EventUpdateSchema(SQLModel):
    description: str
    

class EventModel(SQLModel, table=True):
    # id: int
    id: Optional[int] = Field(default=None, primary_key=True)
    page: Optional[str] = ""
    description: Optional[str] = ""
    

class EventListSchema(SQLModel):
    results: List[EventModel]
    count: int