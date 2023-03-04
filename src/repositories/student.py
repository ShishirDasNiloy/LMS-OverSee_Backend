from models import Student, User
from schemas import StudentIn, StudentUpdate
from repositories import BaseRepo
from sqlalchemy.orm import Session


class StudentRepo(BaseRepo[Student, StudentIn, StudentUpdate]):
    def active_students(self, db: Session, skip: int, limit: int):
        
        data = db.query(self.model).join(User, User.id == self.model.user_id).filter(User.is_active == True).filter(
            User.role_id == 3).offset(skip).limit(limit).all()
        return data
    
    def active_students_count(self, db: Session):
        data_count = db.query(User).filter(
            User.is_active == True).filter(User.role_id == 3).all()
        return {"results": len(data_count)}
    

    def inactive_students(self, db: Session, skip: int, limit: int):
        
        data = db.query(self.model).join(User, User.id == self.model.user_id).filter(User.is_active == False).filter(
            User.role_id == 3).offset(skip).limit(limit).all()
        return data
    
    def inactive_students_count(self, db: Session):
        data_count = db.query(User).filter(
            User.is_active == False).filter(User.role_id == 3).all()
        return {"results": len(data_count)}


student_repo = StudentRepo(Student)
