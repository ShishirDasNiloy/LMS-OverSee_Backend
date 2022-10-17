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