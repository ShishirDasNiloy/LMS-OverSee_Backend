from models import ClassRoomWithUser
from schemas import ClassRoomWithUserIn, ClassRoomWithUserUpdate
from repositories import class_room_with_user_repo
from services import BaseService, class_room_service
from sqlalchemy.orm import Session
from exceptions.service_result import handle_result
from exceptions.service_result import ServiceResult
from exceptions.app_exceptions import AppException

class ClassRoomWithUserService(BaseService[ClassRoomWithUser, ClassRoomWithUserIn, ClassRoomWithUserUpdate]):


    def check_class(self, db: Session, class_room_code: str):
        check = class_room_service.get_by_key(db=db, skip=0, limit=100, descending=False, count_results=False, class_room_code=class_room_code)
        check_class_code = handle_result(check)

        if len(check_class_code) == 1:
            return check_class_code[0].id
        else:
            return False

    def join_class(self, db: Session, user_id:int, class_room_code: str):

        check_class = self.check_class(db=db, class_room_code=class_room_code)
        class_id = check_class
        if check_class == False:
            return ServiceResult(AppException.ServerError("Classroom not found"))

        else:
            stu_add_class = self.repo.create_with_flush(db=db, data_in=ClassRoomWithUserIn(
                class_room_id=class_id,
                user_id=user_id
            ))
        db.commit()
        return ServiceResult({"msg": "Success"}, status_code=200)


        

        


class_room_with_user_service = ClassRoomWithUserService(ClassRoomWithUser, class_room_with_user_repo)
