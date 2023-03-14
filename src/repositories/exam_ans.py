from repositories import BaseRepo
from models import ExamAns
from schemas import ExamAnsIn, ExamAnsUpdate
from sqlalchemy.orm import Session
from sqlalchemy import desc


class ExamAnsRepo(BaseRepo[ExamAns, ExamAnsIn, ExamAnsUpdate]):
    def get_ans_by_exam(self, db: Session, exam_id: int):

        data = db.query(self.model).filter(self.model.exam_id ==  exam_id).all()
        return data



exam_ans_repo = ExamAnsRepo(ExamAns)