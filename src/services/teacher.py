from services import BaseService
from models import Teacher
from schemas import TeacherIn, TeacherUpdate
from repositories import teacher_repo


class TeacherService(BaseService[Teacher, TeacherIn, TeacherUpdate]):
    pass


teacher_service = TeacherService(Teacher, teacher_repo)
