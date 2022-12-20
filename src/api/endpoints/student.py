from fastapi import APIRouter, Depends
from db import get_db
from exceptions.service_result import handle_result
from schemas import StudentSignup, StudentOut, UserLogin, Token
from sqlalchemy.orm import Session
from services import student_service
from typing import List

router = APIRouter()


@router.post('/signup')
def signup_student(student_in: StudentSignup, db: Session = Depends(get_db)):
    student = student_service.student_signup(db=db, data_in=student_in)
    return handle_result(student)


@router.get('/', response_model=List[StudentOut])
def get_student(db: Session = Depends(get_db)):
    get_student = student_service.get(db=db)
    return handle_result(get_student) 



@router.post('/login', response_model=Token)
def login(data_in: UserLogin, db: Session = Depends(get_db)):
    user = student_service.login(db, data_in.identifier, data_in.password)
    return handle_result(user)