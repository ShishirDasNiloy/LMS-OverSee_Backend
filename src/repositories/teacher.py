from models import Teacher
from repositories import BaseRepo
from schemas import TeacherIn, TeacherUpdate


class TeacherRepo(BaseRepo[Teacher, TeacherIn, TeacherUpdate]):
    pass

teacher_repo = TeacherRepo(Teacher)