from fastapi import APIRouter
from .endpoints import users, roles, admin

api_router = APIRouter()

api_router.include_router(users.router, prefix='', tags = ["Users"])
api_router.include_router(roles.router, prefix='/roles', tags=['Roles'])
api_router.include_router(admin.router, prefix='/admin', tags=['Admin'])