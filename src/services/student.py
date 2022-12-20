from models import Student, User
from schemas import StudentIn, StudentUpdate, StudentSignup, UserCreate
from repositories import student_repo
from services import BaseService
from sqlalchemy.orm import Session
from .users import users_service
from exceptions import handle_result, ServiceResult, AppException
from utils import Token


class StudentService(BaseService[Student, StudentIn, StudentUpdate]):
    
    def student_signup(self, db: Session, data_in: StudentSignup):

        signup_data = UserCreate(
            name=data_in.name,
            email=data_in.email,
            phone=data_in.phone,
            sex=data_in.sex,
            is_active=False,
            password=data_in.password,
            role_name='student'
        )

        signup_user = users_service.signup(db=db, data_in=signup_data, flush=True)

        student_data = StudentIn(
            user_id=handle_result(signup_user).id,
            student_id=data_in.student_id,
            department=data_in.department,
            dob=data_in.dob,
            admition_year=data_in.admition_year,
            batch=data_in.batch
        )

        student_create = self.create_with_flush(db=db, data_in=student_data)

        db.commit()
        

    def login(self, db: Session, identifier: str, password: str):
        user: User = users_service.is_auth(db, identifier, password)

        if user and user.is_active == False:
            return ServiceResult(AppException.NotFound("You are not active user."))


        if user is None:
            return ServiceResult(AppException.NotFound("User not found"))
        
        if user.role_id != 3:
            return ServiceResult(AppException.NotFound("Not Student"))


        if user is not None:

            access_token = Token.create_access_token({"sub": user.id})
            return ServiceResult({"access_token": access_token, "token_type": "bearer"}, status_code=200)
        else:
            return ServiceResult(AppException.NotFound("User not found"))


student_service = StudentService(Student, student_repo)