from fastapi import APIRouter, Depends
from db import get_db
from exceptions.service_result import handle_result
from schemas import TeacherSignup, TeacherOut, UserLogin
from sqlalchemy.orm import Session
from services import teacher_service
from typing import List
from schemas import Token

router = APIRouter()

@router.post('/signup')
def signup_teacher(teacher_in: TeacherSignup, db: Session = Depends(get_db)):
    teacher = teacher_service.teacher_signup(db=db, data_in=teacher_in)
    return handle_result(teacher)


@router.get('/', response_model=List[TeacherOut])
def get_teacher(db: Session = Depends(get_db)):
    get_teacher = teacher_service.get(db=db)
    return handle_result(get_teacher)


@router.post('/login', response_model=Token)
def login(data_in: UserLogin, db: Session = Depends(get_db)):
    user = teacher_service.login(db, data_in.identifier, data_in.password)
    return handle_result(user)