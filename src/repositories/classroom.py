from models import ClassRoom
from schemas import ClassRoomIn, ClassRoomUpdate
from repositories import BaseRepo


class ClassRoomRepo(BaseRepo[ClassRoom, ClassRoomIn, ClassRoomUpdate]):
    pass


class_room_repo = ClassRoomRepo(ClassRoom)