from models import ClassRoomWithUser
from schemas import ClassRoomWithUserIn, ClassRoomWithUserUpdate
from repositories import BaseRepo


class_room_with_user_repo = BaseRepo[ClassRoomWithUser, ClassRoomWithUserIn, ClassRoomWithUserUpdate](ClassRoomWithUser)