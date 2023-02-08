from services import BaseService
from .users import users_service
from schemas import UserCreate, UserUpdate
from models import User
from repositories import admin_repo, roles_repo
from sqlalchemy.orm import Session
from exceptions import ServiceResult, AppException
from fastapi import status


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
        data = self.repo.active_teachers(db=db, skip=skip, limit=limit)
        if not data:
            return ServiceResult(AppException.ServerError("no active teacher"))
        else:
            return ServiceResult(data, status_code=status.HTTP_201_CREATED)

    def inactive_teachers(self, db: Session, skip: int, limit: int):
        data = self.repo.inactive_teachers(db=db, skip=skip, limit=limit)
        if not data:
            return ServiceResult(AppException.ServerError("no inactive teacher"))
        else:
            return ServiceResult(data, status_code=status.HTTP_201_CREATED)


    def active_students(self, db: Session, skip: int, limit: int):
        data = self.repo.active_students(db=db, skip=skip, limit=limit)
        if not data:
            return ServiceResult(AppException.ServerError("no active student"))
        else:
            return ServiceResult(data, status_code=status.HTTP_201_CREATED)

    def inactive_students(self, db: Session, skip: int, limit: int):
        data = self.repo.inactive_students(db=db, skip=skip, limit=limit)
        if not data:
            return ServiceResult(AppException.ServerError("no inactive student"))
        else:
            return ServiceResult(data, status_code=status.HTTP_201_CREATED)

    def count_results(self, db: Session):
        data = self.repo.count_results(db=db)
        if not data:
            return ServiceResult(AppException.ServerError("no data"))
        else:
            return ServiceResult(data, status_code=status.HTTP_201_CREATED)



admin_service = Admin(User, admin_repo)
