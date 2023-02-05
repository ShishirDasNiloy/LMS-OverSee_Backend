from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TopicBase(BaseModel):
    class_room_id: int
    created_by: int
    topic_name: str
    topic_type: Optional[str] = None
    topic_details: Optional[str] = None
    image_pdf_string: Optional[str] = None


class TopicIn(TopicBase):
    pass

class TopicCreate(BaseModel):
    class_room_id: int
    topic_name: str
    topic_type: Optional[str] = None
    topic_details: Optional[str] = None
    # image_pdf_string: Optional[str] = None

class TopicUpdate(BaseModel):
    topic_name: Optional[str] = None
    topic_type: Optional[str] = None
    topic_details: Optional[str] = None


class TopicOut(TopicBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True