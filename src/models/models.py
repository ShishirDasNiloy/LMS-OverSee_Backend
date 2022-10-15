from sqlalchemy import Column, String, Boolean
from models.base import BaseModel

class User(BaseModel):
    __tablename__ = "users"
    name = Column(String(100), nullable = False)
    email = Column(String(100), nullable = True)
    phone = Column(String(25), nullable = True)
    password = Column(String(255), nullable = False)
    sex = Column(String(10, nullable = False))
    is_active = Column(Boolean, default = False)