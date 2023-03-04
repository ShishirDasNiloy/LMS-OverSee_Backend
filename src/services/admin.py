from services import BaseService
from .users import users_service
from .teacher import teacher_service
from .student import student_service
from schemas import UserCreate, UserUpdate, TeacherSignup, TeacherIn, StudentSignup, StudentIn
from models import User
from repositories import admin_repo, roles_repo, teacher_repo, users_repo, student_repo
from sqlalchemy.orm import Session
from exceptions import ServiceResult, AppException
from fastapi import status
from exceptions.service_result import handle_result

class Admin(BaseService[User, UserCreate, UserUpdate]):

    def signup_admin(self, db: Session, data_in: UserCreate):

        admin_id = roles_repo.search_name_id(db, name='admin')

        admin_exist = self.repo.search_by_role_id(db, id=admin_id)

        if not admin_exist:
            sginup_data = UserCreate(
                name=data_in.name,
                email=data_in.email,
                phone=data_in.phone,
                sex=data_in.sex,
                is_active=True,
                password=data_in.password,
                role_name='admin'
            )

            signup_admin = users_service.signup(
                db, data_in=sginup_data, flush=False)

            return signup_admin

        return ServiceResult(AppException.ServerError('Admin exist'))


    def user_active_switcher(self, db: Session, id: int):
        data = self.repo.user_active_switcher(db=db, id=id)

        if not data:
            return ServiceResult(AppException.ServerError("User active status not changed"))
        else:
            return ServiceResult(data, status_code=status.HTTP_201_CREATED)
    
    
    def active_teachers(self, db: Session, skip: int, limit: int):
        data = teacher_repo.active_teachers(db=db, skip=skip, limit=limit)

        data_count = teacher_repo.active_teacher_count(db=db)

        all_data = []

        for i in data:
            user_id = i.user_id
            user = users_repo.get_one(db=db, id=user_id)
            i.name = user.name
            i.email = user.email
            i.phone = user.phone
            i.sex = user.sex
            i.is_active = user.is_active
            all_data.append(i)

        # return [data_count, all_data]
        if not data:
            return ServiceResult(AppException.ServerError("no active teacher"))
        else:
            return ServiceResult([data_count, all_data], status_code=status.HTTP_201_CREATED)

    def inactive_teachers(self, db: Session, skip: int, limit: int):
        data = teacher_repo.inactive_teachers(db=db, skip=skip, limit=limit)
        data_count = teacher_repo.inactive_teacher_count(db=db)

        all_data = []

        for i in data:
            user_id = i.user_id
            user = users_repo.get_one(db=db, id=user_id)
            i.name = user.name
            i.email = user.email
            i.phone = user.phone
            i.sex = user.sex
            i.is_active = user.is_active
            all_data.append(i)
        if not data:
            return ServiceResult(AppException.ServerError("no inactive teacher"))
        else:
            return ServiceResult([data_count, all_data], status_code=status.HTTP_201_CREATED)


    def active_students(self, db: Session, skip: int, limit: int):
        data = student_repo.active_students(db=db, skip=skip, limit=limit)
        data_count = student_repo.active_students_count(db=db)

        all_data = []

        for i in data:
            user_id = i.user_id
            user = users_repo.get_one(db=db, id=user_id)
            i.name = user.name
            i.email = user.email
            i.phone = user.phone
            i.sex = user.sex
            i.is_active = user.is_active
            all_data.append(i)
        if not data:
            return ServiceResult(AppException.ServerError("no active student"))
        else:
            return ServiceResult([data_count, all_data], status_code=status.HTTP_201_CREATED)

    def inactive_students(self, db: Session, skip: int, limit: int):
        data = student_repo.inactive_students(db=db, skip=skip, limit=limit)
        data_count = student_repo.inactive_students_count(db=db)

        all_data = []

        for i in data:
            user_id = i.user_id
            user = users_repo.get_one(db=db, id=user_id)
            i.name = user.name
            i.email = user.email
            i.phone = user.phone
            i.sex = user.sex
            i.is_active = user.is_active
            all_data.append(i)
        if not data:
            return ServiceResult(AppException.ServerError("no inactive student"))
        else:
            return ServiceResult([data_count, all_data], status_code=status.HTTP_201_CREATED)

    def count_results(self, db: Session):
        data = self.repo.count_results(db=db)
        if not data:
            return ServiceResult(AppException.ServerError("no data"))
        else:
            return ServiceResult(data, status_code=status.HTTP_201_CREATED)
        
    def teacher_reg(self, db: Session, data_in: TeacherSignup):

        signup_data = UserCreate(
            name=data_in.name,
            email=data_in.email,
            phone=data_in.phone,
            sex=data_in.sex,
            is_active=True,
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

        teacher_create = teacher_service.create_with_flush(db=db, data_in=teacher_data)


        db.commit()
        return ServiceResult({"msg": "Success"}, status_code=200)
    
    def student_reg(self, db: Session, data_in: StudentSignup):

        signup_data = UserCreate(
            name=data_in.name,
            email=data_in.email,
            phone=data_in.phone,
            sex=data_in.sex,
            is_active=True,
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

        student_create = student_service.create_with_flush(db=db, data_in=student_data)

        db.commit()
        return ServiceResult({"msg": "Success"}, status_code=200)



admin_service = Admin(User, admin_repo)
