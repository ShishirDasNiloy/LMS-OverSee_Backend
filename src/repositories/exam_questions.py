from repositories import BaseRepo
from models import ExamQuestions
from schemas import ExamQuestionsIn, ExamQuestionsUpdate
from sqlalchemy.orm import Session
from sqlalchemy import desc



class ExamQuestionsRepo(BaseRepo[ExamQuestions, ExamQuestionsIn, ExamQuestionsUpdate]):
    
    def get_questions_by_exam(self, db: Session, exam_id: int):

        data = db.query(self.model).filter(self.model.exam_id ==  exam_id).all()
        return data



exam_questions_repo = ExamQuestionsRepo(ExamQuestions)