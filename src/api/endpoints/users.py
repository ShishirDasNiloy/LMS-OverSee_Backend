from fastapi import APIRouter


router = APIRouter()

@router.get("/")
def user():
    return {"Hello":"Shishir"}
    