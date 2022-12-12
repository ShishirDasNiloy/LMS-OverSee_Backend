from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TopicBase(BaseModel):
    class_room_id: int
    created_by: str
    topic_name: str
    topic_type: Optional[str] = None
    topic_details: Optional[str] = None


class TopicIn(TopicBase):
    pass

class TopicUpdate(BaseModel):
    topic_name: Optional[str] = None
    topic_type: Optional[str] = None
    topic_details: Optional[str] = None


class TopicOut(TopicBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True