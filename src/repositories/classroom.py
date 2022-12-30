from models import ClassRoom
from schemas import ClassRoomIn, ClassRoomUpdate
from repositories import BaseRepo
from sqlalchemy.orm import Session
from sqlalchemy.sql import desc


class ClassRoomRepo(BaseRepo[ClassRoom, ClassRoomIn, ClassRoomUpdate]):
    
    def classroom_by_teacher_id(self, db: Session, teacher_id: int, skip: int, limit: int):
        data_count = db.query(self.model).filter(self.model.created_by == teacher_id).all()
        data = db.query(self.model).filter(self.model.created_by == teacher_id).order_by(desc(self.model.created_at)).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]


class_room_repo = ClassRoomRepo(ClassRoom)