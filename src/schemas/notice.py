from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class NoticeBase(BaseModel):
    created_by: int
    notice_title: Optional[str] = None
    notice_details: Optional[str] = None


class NoticeIn(NoticeBase):
    pass


class NoticeCreate(BaseModel):
    notice_title: Optional[str] = None
    notice_details: Optional[str] = None


class NoticeUpdate(BaseModel):
    notice_title: Optional[str] = None
    notice_details: Optional[str] = None


class NoticeOut(NoticeBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True