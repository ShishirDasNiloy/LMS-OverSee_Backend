from fastapi import APIRouter, Depends, UploadFile, File
from db import get_db
from exceptions.service_result import handle_result
from schemas import StudentSignup, StudentOut, UserLogin, Token, ExamAnsSubmit
from sqlalchemy.orm import Session
from services import student_service, class_room_with_user_service, exam_with_student_service, exam_ans_service
from typing import List
from api.auth_dependcies import logged_in
from repositories import class_room_repo, exam_repo
from utils import UploadFileUtils
from typing import Optional
from exceptions.service_result import ServiceResult
from exceptions.app_exceptions import AppException

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


@router.post('/join-exam')
def join_exam(exam_code: str, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    je = exam_with_student_service.join_exam(db=db, exam_code=exam_code, user_id = current_user.id)
    return handle_result(je)


@router.get('all-exam')
def get_all_exam(db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    gae = exam_repo.exam_by_student_id(db=db, student_id = current_user.id)
    return gae



@router.post('/submit-exam-ans-pdf')
async def upload_file(exam_id: int, file: Optional[UploadFile] = File(None), db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):

    if file is None:
        new_file_name = ''
    else:
        up_img = UploadFileUtils(file=file)

    # prefix is the short service name
        # new_file_name = up_img.upload_pdf(prefix='exam-ans', path='./assets/pdf', accept_extensions=['pdf'])

    check = exam_ans_service.get_by_two_key(db=db, skip=0, limit=10, descending=False,count_results=False, exam_id=exam_id, user_id = current_user.id)
    temp = handle_result(check)

    if len(temp) == 0 :
    # save in db
        new_file_name = up_img.upload_pdf(prefix='exam-ans', path='./assets/pdf', accept_extensions=['pdf'])
        file_in_db = exam_ans_service.create(db=db, data_in=ExamAnsSubmit(exam_id=exam_id, user_id=current_user.id, ans_file_string=new_file_name))
        print("Created")

    else: 
        print("Already Created")
        return ServiceResult(AppException.ServerError("Already Submited"))

    return handle_result(file_in_db)



@router.get('exam-ans')
def get_exam_ans(exam_id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    gea = exam_ans_service.get_by_two_key(db=db, skip=0, limit=1, descending=False,count_results=False, exam_id=exam_id, user_id = current_user.id)
    return handle_result(gea)