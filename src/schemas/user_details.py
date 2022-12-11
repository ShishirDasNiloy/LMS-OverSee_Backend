from datetime import date
from typing import Optional
from pydantic import BaseModel


class UserDetailBase(BaseModel):    
    fathers_name: Optional[str] = None
    mothers_name: Optional[str] = None
    dob: Optional[date] = None
    blood_group: Optional[str] = None


class UserDetailIn(UserDetailBase):
    user_id: int


class UserDetailUpdate(BaseModel):
    fathers_name: Optional[str] = None
    mothers_name: Optional[str] = None
    dob: Optional[date] = None
    blood_group: Optional[str] = None


class UserDetailOut(UserDetailBase):
    user_id: Optional[int]

    class Config:
        orm_mode = True