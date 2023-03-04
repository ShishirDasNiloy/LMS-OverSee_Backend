from models import Teacher, User
from repositories import BaseRepo
from schemas import TeacherIn, TeacherUpdate
from sqlalchemy.orm import Session


class TeacherRepo(BaseRepo[Teacher, TeacherIn, TeacherUpdate]):
    def active_teachers(self, db: Session, skip: int, limit: int):
        
        data = db.query(self.model).join(User, User.id == self.model.user_id).filter(User.is_active == True).filter(
            User.role_id == 2).offset(skip).limit(limit).all()
        return data
    
    def active_teacher_count(self, db: Session):
        data_count = db.query(User).filter(
            User.is_active == True).filter(User.role_id == 2).all()
        return {"results": len(data_count)}
    

    def inactive_teachers(self, db: Session, skip: int, limit: int):
        
        data = db.query(self.model).join(User, User.id == self.model.user_id).filter(User.is_active == False).filter(
            User.role_id == 2).offset(skip).limit(limit).all()
        return data
    
    def inactive_teacher_count(self, db: Session):
        data_count = db.query(User).filter(
            User.is_active == False).filter(User.role_id == 2).all()
        return {"results": len(data_count)}

teacher_repo = TeacherRepo(Teacher)