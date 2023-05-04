from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional
from pydantic.types import constr


class StudentBase(BaseModel):
    user_id: int
    student_id: Optional[str] = None
    department: Optional[str] = None
    dob: Optional[date] = None
    admition_year: Optional[date] = None
    batch: Optional[str] = None


class StudentIn(StudentBase):
    pass



class StudentUpdate(BaseModel):
    student_id: Optional[str] = None
    department: Optional[str] = None
    dob: Optional[date] = None
    admition_year: Optional[date] = None
    batch: Optional[str] = None


class StudentOut(StudentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class StudentSignup(BaseModel):
    name: str
    email: Optional[str] = None
    phone: constr(min_length=11, max_length=14, regex=r"(^(\+88)?(01){1}[3-9]{1}\d{8})$")
    sex: str
    password: str
    student_id: Optional[str] = None
    department: Optional[str] = None
    dob: Optional[date] = None
    admition_year: Optional[date] = None
    batch: Optional[str] = None