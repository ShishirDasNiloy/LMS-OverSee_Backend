from repositories import BaseRepo
from schemas import UserCreate, UserUpdate
from models import User, Teacher
from sqlalchemy.orm import Session


class AdminRepo(BaseRepo[User, UserCreate, UserUpdate]):

    def search_by_role_id(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.role_id == id).all()

    def user_active_switcher(self, db: Session, id: int):
        current_status = self.get_one(db=db, id=id).is_active
        data = self.update(db=db, id=id, data_update=UserUpdate(
            is_active=not current_status))
        return data

    def active_teachers(self, db: Session, skip: int, limit: int):
        data_count = db.query(self.model).filter(
            self.model.is_active == True).filter(self.model.role_id == 2).all()
        data = db.query(self.model,Teacher).join(Teacher, Teacher.user_id == self.model.id).filter(self.model.is_active == True).filter(
            self.model.role_id == 2).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]

    def inactive_teachers(self, db: Session, skip: int, limit: int):
        data_count = db.query(self.model).filter(
            self.model.is_active == False).filter(self.model.role_id == 2).all()
        data = db.query(self.model).filter(self.model.is_active == False).filter(
            self.model.role_id == 2).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]

    def active_students(self, db: Session, skip: int, limit: int):
        data_count = db.query(self.model).filter(
            self.model.is_active == True).filter(self.model.role_id == 3).all()
        data = db.query(self.model).filter(self.model.is_active == True).filter(
            self.model.role_id == 3).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]

    def inactive_students(self, db: Session, skip: int, limit: int):
        data_count = db.query(self.model).filter(
            self.model.is_active == False).filter(self.model.role_id == 3).all()
        data = db.query(self.model).filter(self.model.is_active == False).filter(
            self.model.role_id == 3).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]

    def count_results(self, db: Session):
        count_total_tea = db.query(self.model).filter(
            self.model.role_id == 2).all()
        count_active_tea = db.query(self.model).filter(
            self.model.is_active == True).filter(self.model.role_id == 2).all()
        count_inactive_tea = db.query(self.model).filter(
            self.model.is_active == False).filter(self.model.role_id == 2).all()
        count_total_stu = db.query(self.model).filter(
            self.model.role_id == 3).all()
        count_active_stu = db.query(self.model).filter(
            self.model.is_active == True).filter(self.model.role_id == 3).all()
        count_inactive_stu = db.query(self.model).filter(
            self.model.is_active == False).filter(self.model.role_id == 3).all()

        return [len(count_total_tea), len(count_active_tea), len(count_inactive_tea), len(count_total_stu), len(count_active_stu), len(count_inactive_stu)]


admin_repo = AdminRepo(User)
