from fastapi import APIRouter
from .endpoints import users, roles, admin, teacher, student

api_router = APIRouter()

api_router.include_router(users.router, prefix='', tags = ["Users"])
api_router.include_router(roles.router, prefix='/roles', tags=['Roles'])
api_router.include_router(admin.router, prefix='/admin', tags=['Admin'])
api_router.include_router(teacher.router, prefix="/teacher", tags=['Teacher'])
api_router.include_router(student.router, prefix="/student", tags=['Student'])