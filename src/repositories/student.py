from models import Student
from schemas import StudentIn, StudentUpdate
from repositories import BaseRepo


class StudentRepo(BaseRepo[Student, StudentIn, StudentUpdate]):
    pass


student_repo = StudentRepo(Student)
