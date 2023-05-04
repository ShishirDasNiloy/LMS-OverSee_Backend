from pydantic import BaseModel
from datetime import datetime


class ClassRoomWithUserBase(BaseModel):
    class_room_id: int
    user_id: int



class ClassRoomWithUserIn(ClassRoomWithUserBase):
    pass


class ClassRoomWithUserUpdate(BaseModel):
    pass


class ClassRoomWithUserOut(ClassRoomWithUserBase):
    id: int
    created_at: datetime