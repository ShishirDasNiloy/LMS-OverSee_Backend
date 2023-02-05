from models import Topic
from schemas import TopicIn, TopicUpdate
from repositories import topic_repo
from services import BaseService
from sqlalchemy.orm import Session
from exceptions import AppException, ServiceResult, handle_result
from fastapi import status, UploadFile, File
from utils import UploadFileUtils


class TopicService(BaseService[Topic, TopicIn, TopicUpdate]):
    
    def create_topic(self, db: Session, data_in: TopicIn, user_id: int, file: UploadFile = File(...)):

        
        up_file = UploadFileUtils(file)
        new_file_name = up_file.upload_image(prefix='topic', path='./assets/img', accepted_extensions=['jpg', 'jpeg', 'png', 'pdf'])

        topic_data = TopicIn(
            class_room_id=data_in.class_room_id,
            created_by= user_id,
            topic_name=data_in.topic_name,
            topic_type=data_in.topic_type,
            topic_details=data_in.topic_details,
            image_pdf_string=new_file_name,
        )

        create_topic = self.create(db=db, data_in=topic_data)

        if not create_topic:
            return ServiceResult(AppException.ServerError("Problem with class creation"))
        else:
            return ServiceResult(handle_result(create_topic), status_code = status.HTTP_201_CREATED)

    def get_topic_by_class(self, db: Session, class_room_id: int):
        get_topic = self.repo.get_topic_by_class(db=db, class_room_id = class_room_id)
        return get_topic

topic_service = TopicService(Topic, topic_repo)