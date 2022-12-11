from repositories import BaseRepo
from models import UserDetail
from schemas import UserDetailIn, UserDetailUpdate

class UserDetailRepo(BaseRepo[UserDetail, UserDetailIn, UserDetailUpdate]):
    pass


user_details_repo = UserDetailRepo(UserDetail)