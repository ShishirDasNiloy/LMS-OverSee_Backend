from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from exceptions import handle_result
from services import roles_service
from schemas.roles import RoleOut, RoleIn, RoleUpdate
from db import get_db
from typing import List
from api.auth_dependcies import  logged_in_admin

router = APIRouter()


@router.get('/', response_model=List[RoleOut])
def get(db: Session = Depends(get_db)):
    roles = roles_service.get(db)
    return handle_result(roles)


@router.post('/', response_model=RoleOut)
def post(role_in: RoleIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    role = roles_service.create(db, data_in=role_in)
    return handle_result(role)


@router.post('/first/{name}', response_model=RoleOut)
def first_role(name: str, db: Session = Depends(get_db)):
    name = roles_service.first_role(db=db, name=name)
    return handle_result(name)
