from pydantic import BaseModel
from datetime import datetime
from typing import Optional



class ClassRoomBase(BaseModel):
    created_by: int
    classroom_name: str
    class_room_code: str
    class_room_details : Optional[str] = None


class ClassRoomIn(ClassRoomBase):
    pass

class ClassRoomCreate(BaseModel):
    classroom_name: Optional[str] = None
    class_room_code: Optional[str] = None
    class_room_details : Optional[str] = None


class ClassRoomUpdate(BaseModel):
    classroom_name: Optional[str] = None
    class_room_code: Optional[str] = None
    class_room_details : Optional[str] = None


class ClassRoomOut(ClassRoomBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True