from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from pydantic.types import constr

class UserBase(BaseModel):
    name: str
    email: Optional[str] = None
    phone: constr(min_length=11, max_length=14, regex=r"(^(\+88)?(01){1}[3-9]{1}\d{8})$")
    sex: str
    is_active: bool


class UserCreate(UserBase):
    password: str
    role_name: str


class UserCreateWitoutRole(UserBase):
    password: str


class UserIn(UserBase):
    password: str
    role_id: int


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    sex: Optional[str] = None
    role_id: Optional[int] = None
    is_active: Optional[bool] = None


class UserOut(UserBase):
    id: int
    phone: str
    role_id: int
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class UserOutAuth(UserBase):
    id: int
    phone: str
    role_name: Optional[str]

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    identifier: str
    password: str


class NewPasswordIn(BaseModel):
    password: str


