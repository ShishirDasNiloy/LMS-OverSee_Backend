from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional


class StudentBase(BaseModel):
    user_id: int
    student_id: Optional[str] = None
    department: Optional[str] = None
    admition_year: Optional[date] = None
    batch: Optional[str] = None


class StudentIn(StudentBase):
    pass



class StudentUpdate(BaseModel):
    student_id: Optional[str] = None
    department: Optional[str] = None
    admition_year: Optional[date] = None
    batch: Optional[str] = None


class StudentOut(StudentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True