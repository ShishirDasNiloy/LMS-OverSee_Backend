from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class ExamBase(BaseModel):
    user_id: int
    course_name: str
    course_code: str
    exam_code: str
    exam_type: str
    total_marks: int
    time: str


class ExamIn(ExamBase):
    pass

class ExamCreate(BaseModel):
    course_name: str
    course_code: str
    exam_code: str
    exam_type: str
    total_marks: int
    time: str

class ExamCreate(BaseModel):
    course_name: str
    course_code: str
    exam_code: str
    exam_type: str
    total_marks: int
    time: str


class ExamUpdate(BaseModel):
    course_name: Optional[str] = None
    course_code: Optional[str] = None
    exam_code: Optional[str] = None
    exam_type: Optional[str] = None
    total_marks: Optional[int] = None
    time: Optional[str] = None


class ExamOut(ExamBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# exam questions


class ExamQuestionsBase(BaseModel):
    question: Optional[str] = None
    mark: Optional[str] = None


class ExamQuestionsIn(ExamQuestionsBase):
    pass


class ExamQuestionsWithExam(ExamQuestionsBase):
    exam_id: int


class ExamQuestionsUpdate(BaseModel):
    question: Optional[str] = None
    mark: Optional[str] = None

class ExamQuestionsOut(ExamQuestionsBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True



class ExamWithQuestions(BaseModel):
    exam : ExamCreate
    exam_questions: List[ExamQuestionsIn]


# Exam Answers
class ExamAnsBase(BaseModel):
    exam_id: int
    user_id: int
    mark: Optional[int]
    ans_file_string: Optional[str] = None

class ExamAnsIn(ExamAnsBase):
    pass

class ExamAnsSubmit(BaseModel):
    exam_id: int
    user_id: int
    mark: Optional[int]
    ans_file_string: Optional[str] = None


class ExamAnsUpdate(BaseModel):
    mark: Optional[int]

class ExamAnsOut(ExamAnsBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


#Exam With Stu

class ExamWithStudentBase(BaseModel):
    exam_id: int
    user_id: int



class ExamWithStudentIn(ExamWithStudentBase):
    pass


class ExamWithStudentUpdate(BaseModel):
    pass


class ExamWithStudentOut(ExamWithStudentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True