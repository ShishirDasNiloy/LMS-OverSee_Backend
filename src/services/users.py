from utils import Token
from sqlalchemy.orm import Session
from exceptions import ServiceResult
from exceptions import AppException
from repositories import users_repo, roles_repo, login_log_repo
from services import BaseService
from models import User
from schemas import UserCreate, UserUpdate, UserIn, LoginLogIn
from utils import password_hash, verify_password
from fastapi import status


class UserService(BaseService[User, UserCreate, UserUpdate]):

    def signup(self, db: Session, data_in: UserCreate, flush: bool):

        # checking email and phone
        if self.repo.search_by_email(db, data_in.email):
            return ServiceResult(AppException.BadRequest("Email already exist."))
        if self.repo.search_by_phone(db, data_in.phone):
            return ServiceResult(AppException.BadRequest("Phone number already exist."))

        # search role id with role name
        role = roles_repo.search_name_id(db, data_in.role_name)

        data_obj = data_in.dict(exclude={"password", "role_name"})
        password = password_hash(data_in.password)
        data_obj.update({"password": password})

        # data: User = None
        if not flush:
            data = self.repo.create(db, data_in=UserIn(
                **data_obj, role_id=role))
        else:
            data = self.repo.create_with_flush(db, data_in=UserIn(
                **data_obj, role_id=role))

        if not data:
            return ServiceResult(AppException.ServerError("Something went wrong!"))
        return ServiceResult(data, status_code=status.HTTP_201_CREATED)


    def is_auth(self, db: Session, identifier: str, password: str):
        user_by_email = self.repo.search_by_email(db, email_in=identifier)
        user_by_phone = self.repo.search_by_phone(db, phone_in=identifier)

        if user_by_email and verify_password(password, user_by_email.password):
            return user_by_email
        elif user_by_phone and verify_password(password, user_by_phone.password):
            return user_by_phone
        else:
            return None

    def login(self, db: Session, identifier: str, password: str):
        user: User = self.is_auth(db, identifier, password)

        # deactive user prevent
        if user and user.is_active == False:
            return ServiceResult(AppException.NotFound("You are not active user."))

        if user is not None:
            # create log
            ll = login_log_repo.create(db=db, data_in=LoginLogIn(user_id=user.id))

            access_token = Token.create_access_token({"sub": user.id})
            return ServiceResult({"access_token": access_token, "token_type": "bearer"}, status_code=200)
        else:
            return ServiceResult(AppException.NotFound("User not found"))


users_service = UserService(User, users_repo)
