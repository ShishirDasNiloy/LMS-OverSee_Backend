from repositories import exam_questions_repo
from services import BaseService
from models import ExamQuestions
from schemas import ExamQuestionsIn, ExamQuestionsUpdate
from sqlalchemy.orm import Session

class ExamQuestionsService(BaseService[ExamQuestions, ExamQuestionsIn, ExamQuestionsUpdate]):
    
    def get_questions_by_exam(self, db: Session, exam_id: int):

        get_question = self.repo.get_questions_by_exam(db=db, exam_id=exam_id)
        return get_question


exam_questions_service = ExamQuestionsService(ExamQuestions, exam_questions_repo)
