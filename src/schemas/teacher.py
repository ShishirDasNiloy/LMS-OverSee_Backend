from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TeacherBase(BaseModel):
    user_id: int
    teacher_id: Optional[str] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    degree: Optional[str] = None
    institute: Optional[str] = None


class TeacherIn(TeacherBase):
    pass


class TeacherUpdate(BaseModel):
    teacher_id: Optional[str] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    degree: Optional[str] = None
    institute: Optional[str] = None


class TeacherOut(TeacherBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True