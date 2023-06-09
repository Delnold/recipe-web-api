from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import Request
from backend.schemas.users import UserCreate
from backend.db.session import get_db
from backend.db.repository.users import create_new_user

router = APIRouter()

@router.post("/")
def create_user(user : UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user,db=db)
    return user

@router.post("/register/")
def register(request: Request):
    pass