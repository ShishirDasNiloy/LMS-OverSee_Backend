from models import ClassRoom, ClassRoomWithUser
from schemas import ClassRoomIn, ClassRoomUpdate
from repositories import BaseRepo
from sqlalchemy.orm import Session
from sqlalchemy.sql import desc


class ClassRoomRepo(BaseRepo[ClassRoom, ClassRoomIn, ClassRoomUpdate]):
    
    def classroom_by_teacher_id(self, db: Session, teacher_id: int, skip: int, limit: int):
        data_count = db.query(self.model).filter(self.model.created_by == teacher_id).all()
        data = db.query(self.model).filter(self.model.created_by == teacher_id).order_by(desc(self.model.created_at)).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]

    def classroom_by_teacher(self, db: Session, user_id: int):
        data = db.query(self.model).filter(self.model.created_by == user_id).order_by(desc(self.model.created_at)).all()
        return data

    def classroom_by_student_id(self, db: Session, student_id: int):
        data = db.query(self.model).join(ClassRoomWithUser, ClassRoomWithUser.class_room_id == self.model.id).filter(ClassRoomWithUser.user_id == student_id).order_by(desc(ClassRoomWithUser.id)).all()
        return data



class_room_repo = ClassRoomRepo(ClassRoom)