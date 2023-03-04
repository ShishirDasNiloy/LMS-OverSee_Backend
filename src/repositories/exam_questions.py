from repositories import BaseRepo
from models import ExamQuestions
from schemas import ExamQuestionsIn, ExamQuestionsUpdate
from sqlalchemy.orm import Session
from sqlalchemy import desc



class ExamQuestionsRepo(BaseRepo[ExamQuestions, ExamQuestionsIn, ExamQuestionsUpdate]):
    pass


exam_questions_repo = ExamQuestionsRepo(ExamQuestions)