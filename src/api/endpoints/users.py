from fastapi import APIRouter
from fastapi.security import HTTPBasic
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from exceptions import handle_result
from schemas import Token
from models import User
from schemas import UserOut, UserCreate, UserLogin, UserOutAuth
from services import users_service
from api.auth_dependcies import logged_in

router = APIRouter()
security = HTTPBasic()

@router.post('/signup', response_model=UserOut)
def signup(data_in: UserCreate, db: Session = Depends(get_db)):
    user = users_service.signup(db, data_in)
    return handle_result(user)


@router.post('/login', response_model=Token)
def login(data_in: UserLogin, db: Session = Depends(get_db)):
    user = users_service.login(db, data_in.identifier, data_in.password)
    return handle_result(user)


@router.get('/auth', response_model=UserOutAuth)
def auth(current_user: User = Depends(logged_in)):
    return current_user
    