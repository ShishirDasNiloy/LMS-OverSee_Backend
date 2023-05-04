from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional
from pydantic.types import constr


class TeacherBase(BaseModel):
    user_id: int
    teacher_id: Optional[str] = None
    department: Optional[str] = None
    dob: Optional[date] = None
    designation: Optional[str] = None
    degree: Optional[str] = None
    institute: Optional[str] = None


class TeacherIn(TeacherBase):
    pass


class TeacherUpdate(BaseModel):
    teacher_id: Optional[str] = None
    department: Optional[str] = None
    dob: Optional[date] = None
    designation: Optional[str] = None
    degree: Optional[str] = None
    institute: Optional[str] = None


class TeacherOut(TeacherBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True



class TeacherSignup(BaseModel):
    name: str
    email: Optional[str] = None
    phone: constr(min_length=11, max_length=14, regex=r"(^(\+88)?(01){1}[3-9]{1}\d{8})$")
    sex: str
    password: str
    teacher_id: Optional[str] = None
    department: Optional[str] = None
    dob: Optional[date] = None
    designation: Optional[str] = None
    degree: Optional[str] = None
    institute: Optional[str] = None