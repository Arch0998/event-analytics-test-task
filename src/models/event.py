from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class EventCreate(BaseModel):
    event_id: UUID
    occurred_at: datetime
    user_id: str = Field(min_length=1, description="User ID")
    event_type: str = Field(
        min_length=1, description="Event type (click, view, purchase)"
    )
    properties: dict = Field(
        default_factory=dict, description="Additional event properties"
    )


class Event(EventCreate):
    pass
