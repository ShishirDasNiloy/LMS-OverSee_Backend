from models import Notice
from schemas import NoticeIn, NoticeUpdate
from repositories import notice_repo
from services import BaseService
from sqlalchemy.orm import Session
from exceptions import AppException, ServiceResult, handle_result
from fastapi import status

class NoticeService(BaseService[Notice, NoticeIn, NoticeUpdate]):

    def create_notice_teacher(self, db: Session, data_in: NoticeIn, user_id: int):

        notice_data = NoticeIn(
            created_by=user_id,
            notice_title=data_in.notice_title,
            notice_details=data_in.notice_details
        )

        create_notice = self.create(db=db, data_in=notice_data)

        if not create_notice:
            return ServiceResult(AppException.ServerError("Problem with notice creation"))
        else:
            return ServiceResult(handle_result(create_notice), status_code = status.HTTP_201_CREATED)


    def notice_by_teacher(self, db: Session, user_id: int):
        get_notice = self.repo.notice_by_teacher(db=db, user_id=user_id)
        return get_notice


    def all_notice(self, db: Session):
        get_an = self.repo.all_notice(db=db)
        return get_an


notice_service = NoticeService(Notice, notice_repo)

