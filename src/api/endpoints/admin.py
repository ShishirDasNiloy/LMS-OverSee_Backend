from fastapi import APIRouter, Depends
from db import get_db
from exceptions.service_result import handle_result
from schemas import UserOut, UserCreateWitoutRole
from sqlalchemy.orm import Session
from services import admin_service


router = APIRouter()


@router.post('/', response_model=UserOut)
def signup(data_in: UserCreateWitoutRole, db: Session = Depends(get_db)):
    admn = admin_service.signup_admin(db, data_in=data_in)
    return handle_result(admn)