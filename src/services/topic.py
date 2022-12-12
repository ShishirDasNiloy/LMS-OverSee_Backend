from models import Topic
from schemas import TopicIn, TopicUpdate
from repositories import topic_repo
from services import BaseService


class TopicService(BaseService[Topic, TopicIn, TopicUpdate]):
    pass


topic_service = TopicService(Topic, topic_repo)