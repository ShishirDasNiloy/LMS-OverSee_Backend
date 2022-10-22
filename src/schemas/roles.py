from pydantic import BaseModel
from typing import Optional

class RoleBase(BaseModel):
    name: str

class RoleIn(RoleBase):
    pass


class RoleUpdate(BaseModel):
    name: Optional[str]

    class Config:
        orm_mode = True


class RoleOut(RoleBase):
    id: Optional[int]

    class Config:
        orm_mode = True
