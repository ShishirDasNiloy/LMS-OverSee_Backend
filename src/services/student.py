from models import Student
from schemas import StudentIn, StudentUpdate
from repositories import student_repo
from services import BaseService


class StudentService(BaseService[Student, StudentIn, StudentUpdate]):
    pass


student_service = StudentService(Student, student_repo)