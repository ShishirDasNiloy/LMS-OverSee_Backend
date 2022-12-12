from repositories import user_details_repo
from services import BaseService
from models import UserDetail
from schemas import UserDetailIn, UserDetailUpdate

class UserDetailService(BaseService[UserDetail, UserDetailIn, UserDetailUpdate]):
    pass


user_details_service = UserDetailService(UserDetail, user_details_repo)
