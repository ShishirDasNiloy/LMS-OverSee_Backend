from services import BaseService
from models import Teacher, User
from schemas import TeacherIn, TeacherUpdate, TeacherSignup, UserCreate
from repositories import teacher_repo
from sqlalchemy.orm import Session
from .users import users_service
from exceptions import handle_result, ServiceResult, AppException
from utils import Token


class TeacherService(BaseService[Teacher, TeacherIn, TeacherUpdate]):
    
    def teacher_signup(self, db: Session, data_in: TeacherSignup):

        signup_data = UserCreate(
            name=data_in.name,
            email=data_in.email,
            phone=data_in.phone,
            sex=data_in.sex,
            is_active=False,
            password=data_in.password,
            role_name='teacher'
        )

        signup_user = users_service.signup(db=db, data_in=signup_data, flush=True)

        teacher_data = TeacherIn(
            user_id=handle_result(signup_user).id,
            teacher_id=data_in.teacher_id,
            department=data_in.department,
            dob=data_in.dob,
            designation=data_in.designation,
            degree=data_in.degree,
            institute=data_in.institute

        )

        teacher_create = self.create_with_flush(db=db, data_in=teacher_data)


        db.commit()
        return ServiceResult({"msg": "Success"}, status_code=200)

    def login(self, db: Session, identifier: str, password: str):
        user: User = users_service.is_auth(db, identifier, password)

        if user and user.is_active == False:
            return ServiceResult(AppException.NotFound("You are not active user."))

        if user is None:
            return ServiceResult(AppException.NotFound("User not found"))
        
        if user.role_id != 2:
            return ServiceResult(AppException.NotFound("Not Teacher"))

        if user is not None:

            access_token = Token.create_access_token({"sub": user.id})
            return ServiceResult({"access_token": access_token, "token_type": "bearer"}, status_code=200)
        else:
            return ServiceResult(AppException.NotFound("User not found"))


teacher_service = TeacherService(Teacher, teacher_repo)
