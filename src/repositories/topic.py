from models import Topic
from schemas import TopicIn, TopicUpdate
from repositories import BaseRepo


class TopicRepo(BaseRepo[Topic, TopicIn, TopicUpdate]):
    pass


topic_repo = TopicRepo(Topic)