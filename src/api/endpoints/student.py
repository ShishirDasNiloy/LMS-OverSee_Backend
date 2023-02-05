from fastapi import APIRouter, Depends
from db import get_db
from exceptions.service_result import handle_result
from schemas import StudentSignup, StudentOut, UserLogin, Token, ClassRoomWithUserIn
from sqlalchemy.orm import Session
from services import student_service, class_room_with_user_service, class_room_service
from typing import List
from api.auth_dependcies import logged_in
from repositories import class_room_repo

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


@router.get('/class')
def check_class(class_room_code: str, db: Session = Depends(get_db)):
    check_class = class_room_with_user_service.check_class(db=db, class_room_code=class_room_code)
    return check_class

@router.post('/join-class')
def join_class(class_roon_code: str, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    jc = class_room_with_user_service.join_class(db=db, class_room_code=class_roon_code, user_id = current_user.id)
    return handle_result(jc)

@router.get('all-classroom')
def get_all_classroom(db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    gac = class_room_repo.classroom_by_student_id(db=db, student_id = current_user.id)
    return gac
