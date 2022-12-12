from models import TopicDiscuss
from schemas import TopicDiscussIn, TopicDiscussUpdate
from repositories import topic_discuss_repo
from services import BaseService


topic_discuss_service = BaseService[TopicDiscuss, TopicDiscussIn, TopicDiscussUpdate](TopicDiscuss, topic_discuss_repo)