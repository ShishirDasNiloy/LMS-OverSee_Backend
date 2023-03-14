from repositories import BaseRepo
from models import Exam, ExamWithStudent
from schemas import ExamIn, ExamUpdate
from sqlalchemy.orm import Session
from sqlalchemy import desc



class ExamRepo(BaseRepo[Exam, ExamIn, ExamUpdate]):
    def exam_by_teacher(self, db: Session, user_id: int):
        data = db.query(self.model).filter(self.model.user_id == user_id).order_by(desc(self.model.created_at)).all()
        return data
    
    def exam_by_student_id(self, db: Session, student_id: int):
        data = db.query(self.model).join(ExamWithStudent, ExamWithStudent.exam_id == self.model.id).filter(ExamWithStudent.user_id == student_id).order_by(desc(ExamWithStudent.id)).all()
        return data


exam_repo = ExamRepo(Exam)