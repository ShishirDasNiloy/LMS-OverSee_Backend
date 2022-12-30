
from models import ClassRoom
from schemas import ClassRoomIn, ClassRoomUpdate
from repositories import class_room_repo
from services import BaseService
from sqlalchemy.orm import Session
from exceptions import AppException, ServiceResult, handle_result
from fastapi import status


class ClassRoomService(BaseService[ClassRoom, ClassRoomIn, ClassRoomUpdate]):
    
    def create_classroom_teacher(self, db: Session, data_in: ClassRoomIn, user_id: int):

        class_room_data = ClassRoomIn(
            created_by=user_id,
            classroom_name=data_in.classroom_name,
            class_room_code=data_in.class_room_code,
            class_room_details=data_in.class_room_details
        )

        create_classroom = self.create(db=db, data_in=class_room_data)

        if not create_classroom:
            return ServiceResult(AppException.ServerError("Problem with class creation"))
        else:
            return ServiceResult(handle_result(create_classroom), status_code = status.HTTP_201_CREATED)

    def classroom_by_teacher_id(self, db: Session, teacher_id: int, skip: int, limit: int):
        get_classroom = self.repo.classroom_by_teacher_id(db=db, teacher_id=teacher_id, skip=skip, limit=limit)
        return get_classroom

class_room_service = ClassRoomService(ClassRoom, class_room_repo)