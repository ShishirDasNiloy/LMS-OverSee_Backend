from models import Topic
from schemas import TopicIn, TopicUpdate
from repositories import BaseRepo
from sqlalchemy.orm import Session
from sqlalchemy.sql import desc


class TopicRepo(BaseRepo[Topic, TopicIn, TopicUpdate]):
    
    def get_topic_by_class(self, db: Session, class_room_id: int):
        data = db.query(self.model).filter(self.model.class_room_id == class_room_id).order_by(desc(self.model.id)).all()
        return data


topic_repo = TopicRepo(Topic)