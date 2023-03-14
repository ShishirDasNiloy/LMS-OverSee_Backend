from repositories import exam_with_student_repo
from services import BaseService, exam_service
from models import ExamWithStudent
from schemas import ExamWithStudentIn, ExamWithStudentUpdate
from sqlalchemy.orm import Session
from exceptions.service_result import handle_result
from exceptions.service_result import ServiceResult
from exceptions.app_exceptions import AppException

class ExamWithStudentService(BaseService[ExamWithStudent, ExamWithStudentIn, ExamWithStudentUpdate]):
    
    def check_exam(self, db: Session, exam_code: str):
        check = exam_service.get_by_key(db=db, skip=0, limit=100, descending=False, count_results=False, exam_code=exam_code)
        check_exam_code = handle_result(check)

        if len(check_exam_code) == 1:
            return check_exam_code[0].id
        else:
            return False

    def join_exam(self, db: Session, user_id:int, exam_code: str):

        check_exam = self.check_exam(db=db, exam_code=exam_code)
        exam_id = check_exam
        if check_exam == False:
            return ServiceResult(AppException.ServerError("Exam not found"))

        else:
            stu_add_exam = self.repo.create_with_flush(db=db, data_in=ExamWithStudentIn(
                exam_id=exam_id,
                user_id=user_id
            ))
        db.commit()
        return ServiceResult({"msg": "Success"}, status_code=200)


exam_with_student_service = ExamWithStudentService(ExamWithStudentService, exam_with_student_repo)
