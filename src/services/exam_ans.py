from repositories import exam_ans_repo, student_repo, users_repo
from services import BaseService
from models import ExamAns
from schemas import ExamAnsIn, ExamAnsUpdate
from sqlalchemy.orm import Session
from exceptions import ServiceResult, AppException
from fastapi import status
from exceptions.service_result import handle_result

class ExamAnsService(BaseService[ExamAns, ExamAnsIn, ExamAnsUpdate]):
    
    def exam_ans(self, db: Session, exam_id: int):

        data = exam_ans_repo.get_ans_by_exam(db=db, exam_id=exam_id)

        all_data = []

        for i in data:
            user_id = i.user_id
            user = users_repo.get_one(db=db, id=user_id)
            student = student_repo.get_by_key(db=db, skip=0, limit=10, descending=False, count_results=False, user_id= user_id)
            i.name = user.name
            i.student_id = student[0].student_id
            all_data.append(i)

        if not data:
            return ServiceResult(AppException.ServerError("no data"))
        else:
            return ServiceResult(all_data, status_code=status.HTTP_201_CREATED)




exam_ans_service = ExamAnsService(ExamAns, exam_ans_repo)
