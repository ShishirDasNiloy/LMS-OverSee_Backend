from fastapi import APIRouter, Depends
from db import get_db
from exceptions.service_result import handle_result
from schemas import UserOut, UserCreateWitoutRole, ResultInt, TeacherSignup, StudentSignup
from sqlalchemy.orm import Session
from services import admin_service
from typing import List, Union
from repositories import teacher_repo
from api.auth_dependcies import logged_in_admin


router = APIRouter()


@router.post('/', response_model=UserOut)
def signup(data_in: UserCreateWitoutRole, db: Session = Depends(get_db)):
    admn = admin_service.signup_admin(db, data_in=data_in)
    return handle_result(admn)



@router.patch('/switch/active/{id}', response_model=UserOut)
def user_active_switcher(id: int, db: Session = Depends(get_db)):
    act = admin_service.user_active_switcher(db=db, id=id)
    return handle_result(act)

# response_model=List[Union[ResultInt, List[UserOut]]]
@router.get('/active-teacher' )
def active_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    at = admin_service.active_teachers(db=db, skip=skip, limit=limit)
    # at = teacher_repo.active_teachers(db=db, skip=skip, limit=limit)
    return handle_result(at)

# response_model=List[Union[ResultInt, List[UserOut]]]
@router.get('/inactive-teacher' )
def inactive_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    iat = admin_service.inactive_teachers(db=db, skip=skip, limit=limit)
    return handle_result(iat)

# response_model=List[Union[ResultInt, List[UserOut]]]
@router.get('/active-student' )
def active_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    at = admin_service.active_students(db=db, skip=skip, limit=limit)
    return handle_result(at)


@router.get('/inactive-student')
def inactive_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    iat = admin_service.inactive_students(db=db, skip=skip, limit=limit)
    return handle_result(iat)

@router.get('/dashboard/results')
def count_results(db: Session = Depends(get_db)):
    cs = admin_service.count_results(db=db)
    return handle_result(cs)

@router.post('/teacher/reg')
def teacher_reg(teacher_in: TeacherSignup, db: Session = Depends(get_db)):
    teacher = admin_service.teacher_reg(db=db, data_in=teacher_in)
    return handle_result(teacher)


@router.post('/student/reg')
def student_reg(student_in: StudentSignup, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    student = admin_service.student_reg(db=db, data_in=student_in)
    return handle_result(student)