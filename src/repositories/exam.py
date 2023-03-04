from repositories import BaseRepo
from models import Exam
from schemas import ExamIn, ExamUpdate
from sqlalchemy.orm import Session
from sqlalchemy import desc



class ExamRepo(BaseRepo[Exam, ExamIn, ExamUpdate]):
    def exam_by_teacher(self, db: Session, user_id: int):
        data = db.query(self.model).filter(self.model.user_id == user_id).order_by(desc(self.model.created_at)).all()
        return data


exam_repo = ExamRepo(Exam)