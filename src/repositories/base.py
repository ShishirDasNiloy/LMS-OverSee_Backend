import queue
from typing import Any, Generic, Optional, Tuple, Type, TypeVar, List, Union
from sqlalchemy import desc
from sqlalchemy.orm import Session
from db import Base
from models import BaseModel
from .base_abstruct import ABSRepo


ModelType = TypeVar('ModelType', bound = Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound = BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseRepo(Generic[ModelType, CreateSchemaType, UpdateSchemaType], ABSRepo):

    def __init__(self, model: Type[ModelType]):
        self.model = model


    def create(self, db: Session, data_in: CreateSchemaType) -> ModelType:
        data = self.model(**data_in.dict())
        db.add(data)
        db.commit()
        db.refresh(data)
        return data

    def create_with_flush(self, db: Session, data_in: CreateSchemaType):
        data = self.model(**data_in.dict())
        db.add(data)
        db.flush()
        return data

    def create_commit_after_flush(self, db: Session, data_obj: ModelType):
        db.commit()
        db.refresh(data_obj)
        return data_obj


    def get(self, db: Session) -> List[ModelType]:
        query = db.query(self.model).all()
        return query


    def get_one(self, db: Session, id: int) -> ModelType:
        return db.query(self.model).filter(self.model.id == id).first()


    def get_with_pagination(self, db: Session, skip: int, limit: int, descending: bool = False, count_results: bool = False):
        
        query = db.query(self.model).all()

        if descending == True:
            data = db.query(self.model).order_by(
                desc(self.model.created_at)).offset(skip).limit(limit).all()
        else:
            data = db.query(self.model).offset(skip).limit(limit).all()

        if count_results == True:
            return [{"results": len(query)}, data]
        return data
