from fastapi import APIRouter, Depends, UploadFile, File
from db import get_db
from exceptions.service_result import handle_result
from schemas import TeacherSignup, TeacherOut, UserLogin, ClassRoomCreate, TopicCreate, TopicIn, NoticeCreate, ExamWithQuestions
from sqlalchemy.orm import Session
from services import teacher_service, class_room_service, topic_service, notice_service, exam_service
from typing import List
from schemas import Token
from api.auth_dependcies import logged_in_teacher, logged_in
from utils import UploadFileUtils
from typing import Optional
from repositories import exam_repo

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

@router.get('/classroom_by_user/')
def get_classroom(db: Session = Depends(get_db), current_user: Session = Depends(logged_in_teacher)):
    get_class = class_room_service.classroom_by_teacher(db=db, user_id=current_user.id)
    return get_class

@router.get('all-classroom')
def get_all_classroom(teacher_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    gac = class_room_service.classroom_by_teacher_id(db=db, teacher_id=teacher_id, skip=skip, limit=limit)
    return gac

@router.get('/classes')
def get_all(db: Session = Depends(get_db)):
    get = class_room_service.get(db=db)
    return handle_result(get)


@router.post('/create-topic')
async def create_topic(data_in: TopicCreate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_teacher)):
    ct = topic_service.create_topic(db=db, data_in = data_in, user_id=current_user.id)
    return ct

@router.get('/topic-by-class')
def get_all(class_room_id: int, db: Session = Depends(get_db)):
    gt = topic_service.get_topic_by_class(db=db, class_room_id=class_room_id)
    return gt


@router.post('/create_topic-with-file')
async def upload_file(class_room_id: int, topic_name: str, topic_type: Optional[str] = None, topic_details: Optional[str] = None, file: Optional[UploadFile] = File(None), db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):

    if file is None:
        new_file_name = ''
    else:
        up_img = UploadFileUtils(file=file)

    # prefix is the short service name
        new_file_name = up_img.upload_files(prefix='topic', path='./assets/files', accept_extensions=['jpg', 'jpeg', 'png', 'pdf'])


    # save in db
    file_in_db = topic_service.create(db=db, data_in=TopicIn(class_room_id=class_room_id, created_by=current_user.id, topic_name=topic_name, topic_type=topic_type, topic_details=topic_details, image_pdf_string=new_file_name))

    return handle_result(file_in_db)


@router.post('/create-notice')
def create_class(data_in: NoticeCreate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_teacher)):
    cn = notice_service.create_notice_teacher(db=db, data_in=data_in, user_id=current_user.id)
    return handle_result(cn)

@router.get('/notice_by_user/')
def get_notice(db: Session = Depends(get_db), current_user: Session = Depends(logged_in_teacher)):
    get_notice = notice_service.notice_by_teacher(db=db, user_id=current_user.id)
    return get_notice

@router.get('/all-notice')
def get_all_notice(db: Session = Depends(get_db)):
    gan = notice_service.all_notice(db=db)
    return gan


@router.post("/create-exam")
def creat_exam(data_in: ExamWithQuestions, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    ce = exam_service.create_exam(db=db, data_in=data_in,user_id=current_user.id)
    return handle_result(ce)

@router.get('/exams_by_user/')
def get_exams(db: Session = Depends(get_db), current_user: Session = Depends(logged_in_teacher)):
    get_exam = exam_repo.exam_by_teacher(db=db, user_id=current_user.id)
    return get_exam