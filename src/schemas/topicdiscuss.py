# from pydantic import BaseModel
# from datetime import datetime
# from typing import Optional


# class TopicDiscussBase(BaseException):
#     topic_id: int
#     user_id: int
#     discussion_details: Optional[str] = None


# class TopicDiscussIn(TopicDiscussBase):
#     pass



# class TopicDiscussUpdate(BaseModel):
#     discussion_details: Optional[str] = None


# class TopicDiscussOut(TopicDiscussBase):
#     id: int
#     created_at: datetime

#     class Config:
#         orm_mode = True