from repositories import BaseRepo
from models import ExamWithStudent
from schemas import ExamWithStudentIn, ExamWithStudentUpdate
from sqlalchemy.orm import Session
from sqlalchemy import desc


class ExamWithStudentRepo(BaseRepo[ExamWithStudent, ExamWithStudentIn, ExamWithStudentUpdate]):
    pass


exam_with_student_repo = ExamWithStudentRepo(ExamWithStudent)