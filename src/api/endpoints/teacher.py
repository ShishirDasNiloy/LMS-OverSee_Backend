from fastapi import APIRouter, Depends
from db import get_db
from exceptions.service_result import handle_result
from schemas import TeacherSignup, TeacherOut, UserLogin, ClassRoomCreate
from sqlalchemy.orm import Session
from services import teacher_service, class_room_service
from typing import List
from schemas import Token
from api.auth_dependcies import logged_in_teacher

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


@router.post('/create-classroom')
def create_class(data_in: ClassRoomCreate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_teacher)):
    cc = class_room_service.create_classroom_teacher(db=db, data_in=data_in, user_id=current_user.id)
    return handle_result(cc)

@router.get('all-classroom')
def get_all_classroom(teacher_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    gac = class_room_service.classroom_by_teacher_id(db=db, teacher_id=teacher_id, skip=skip, limit=limit)
    return gac
