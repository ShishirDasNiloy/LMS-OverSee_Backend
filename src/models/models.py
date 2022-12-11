from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date, Text
from models.base import BaseModel
from sqlalchemy.orm import relationship

class User(BaseModel):
    __tablename__ = "users"
    name = Column(String(100), nullable = False)
    email = Column(String(100), nullable = True)
    phone = Column(String(25), nullable = True)
    password = Column(String(255), nullable = False)
    sex = Column(String(10), nullable = False)
    is_active = Column(Boolean, default = False)
    role_id = Column(Integer, ForeignKey("roles.id"))

    role = relationship("Role", back_populates="user")
    user_details = relationship("UserDetail", back_populates="user")
    teacher = relationship("Teacher", back_populates = "user_teacher")
    student = relationship("Student", back_populates = "user_student")


class Role(BaseModel):
    __tablename__ = "roles"
    name = Column(String(100), nullable = False, unique = True)

    user = relationship("User", back_populates = "role")


class UserDetail(BaseModel):
    __tablename__ = "user_details"
    user_id = Column(Integer, ForeignKey("users.id"))
    fathers_name = Column(String(100), nullable = True)
    mothers_name = Column(String(100), nullable = True)
    dob = Column(Date, nullable=True)
    blood_group = Column(String(5), nullable=True)

    user = relationship("User", back_populates="user_details")


class LoginLog(BaseModel):
    __tablename__ = "login_log"
    user_id = Column(Integer, ForeignKey("users.id"))


class Teacher(BaseModel):
    __tablename__ = "teachers"
    user_id = Column(Integer, ForeignKey("users.id"))
    teacher_id = Column(String(20), nullable = True)
    designation = Column(String(50), nullable = True)
    degree = Column(String(255), nullable=True)
    institute = Column(String(255), nullable = True)


    user_teacher = relationship("User", back_populates = "teacher")



class Stdent(BaseModel):
    __tablename__ = "students"
    user_id = Column(Integer, ForeignKey("users.id"))
    student_id = Column(String(20), nullable = True)
    admition_year = Column(Date, nullable = True)
    batch = Column(String(20), nullable = True)

    user_student = relationship("User", back_populates = "student")


class ClassRoom(BaseModel):
    __tablename__ = "class_room"
    created_by =  Column(Integer, nullable = False)
    classroom_name = Column(String(255), nullable = False)
    class_room_code = Column(String(100), nullable = False)
    class_room_details = Column(Text, nullable = True)



class ClassRoomWithUser(BaseModel):
    __tablename__ = "class_room_with_user"
    class_room_id = Column(Integer, ForeignKey("class_room.id"))
    user_id = Column(Integer, ForeignKey("users.id"))


class Topic(BaseModel):
    __tablename__ = "topic"
    class_room_id = Column(Integer, ForeignKey("class_room.id"))
    created_by =  Column(Integer, nullable = False)
    topic_name = Column(String, nullable = False)
    topic_type = Column(String, nullable = True)
    topic_details = Column(Text, nullable = True)


class TopicDiscuss(BaseModel):
    __tablename__ = "topic_discuss"
    topic_id = Column(Integer, ForeignKey("topic.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    discussion_details = Column(Text, nullable = True)