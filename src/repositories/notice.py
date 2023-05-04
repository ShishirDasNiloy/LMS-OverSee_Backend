from models import Notice
from schemas import NoticeIn, NoticeUpdate
from repositories import BaseRepo
from sqlalchemy.orm import Session
from sqlalchemy.sql import desc


class NoticeRepo(BaseRepo[Notice, NoticeIn, NoticeUpdate]):

    def notice_by_teacher(self, db: Session, user_id: int):
        data = db.query(self.model).filter(self.model.created_by == user_id).order_by(desc(self.model.created_at)).all()
        return data

    def all_notice(self, db: Session):
        data = db.query(self.model).order_by(desc(self.model.created_at)).all()
        return data


notice_repo = NoticeRepo(Notice)