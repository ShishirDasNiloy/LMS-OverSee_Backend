from services import BaseService
from models import Exam
from schemas import ExamIn, ExamUpdate, ExamWithQuestions, ExamQuestionsWithExam
from repositories import exam_repo, exam_questions_repo
from sqlalchemy.orm import Session
from exceptions.service_result import ServiceResult



class ExamService(BaseService[Exam, ExamIn, ExamUpdate]):
    

    def create_exam(self, data_in: ExamWithQuestions, db: Session, user_id: int):


        exam = exam_repo.create_with_flush(db=db, data_in=ExamIn(
            user_id=user_id,
            course_name=data_in.exam.course_name,
            course_code=data_in.exam.course_code,
            exam_code=data_in.exam.exam_code,
            exam_type=data_in.exam.exam_type,
            total_marks=data_in.exam.total_marks,
            time=data_in.exam.time

        ))

        if data_in.exam_questions and len(data_in.exam_questions) != 0:
            for i in data_in.exam_questions:
                questions = exam_questions_repo.create_with_flush(db=db, data_in=ExamQuestionsWithExam(
                    question=i.question,
                    mark=i.mark,
                    exam_id=exam.id
                ))

        db.commit()

        return ServiceResult({"msg": "Success"}, status_code=200)





exam_service = ExamService(Exam, exam_repo)