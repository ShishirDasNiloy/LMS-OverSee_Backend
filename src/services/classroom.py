
from models import ClassRoom
from schemas import ClassRoomIn, ClassRoomUpdate
from repositories import class_room_repo
from services import BaseService


class ClassRoomService(BaseService[ClassRoom, ClassRoomIn, ClassRoomUpdate]):
    pass


class_room_service = ClassRoomService(ClassRoom, class_room_repo)