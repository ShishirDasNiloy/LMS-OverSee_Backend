from fastapi import APIRouter, Depends
from db import get_db
from exceptions.service_result import handle_result
from schemas import UserOut, UserCreateWitoutRole, ResultInt
from sqlalchemy.orm import Session
from services import admin_service
from typing import List, Union


router = APIRouter()


@router.post('/', response_model=UserOut)
def signup(data_in: UserCreateWitoutRole, db: Session = Depends(get_db)):
    admn = admin_service.signup_admin(db, data_in=data_in)
    return handle_result(admn)



@router.patch('/switch/active/{id}', response_model=UserOut)
def user_active_switcher(id: int, db: Session = Depends(get_db)):
    act = admin_service.user_active_switcher(db=db, id=id)
    return handle_result(act)


@router.get('/active-teacher', response_model=List[Union[ResultInt, List[UserOut]]])
def active_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    at = admin_service.active_teachers(db=db, skip=skip, limit=limit)
    return handle_result(at)


@router.get('/inactive-teacher', response_model=List[Union[ResultInt, List[UserOut]]])
def inactive_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    iat = admin_service.inactive_teachers(db=db, skip=skip, limit=limit)
    return handle_result(iat)


@router.get('/active-student', response_model=List[Union[ResultInt, List[UserOut]]])
def active_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    at = admin_service.active_students(db=db, skip=skip, limit=limit)
    return handle_result(at)


@router.get('/inactive-student', response_model=List[Union[ResultInt, List[UserOut]]])
def inactive_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    iat = admin_service.inactive_students(db=db, skip=skip, limit=limit)
    return handle_result(iat)