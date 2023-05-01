from sqlalchemy.orm import Session
from backend.schemas.users import UserCreate
from backend.db.models import User
from backend.core.password_manager import encrypt_password


def create_new_user(user:UserCreate, db:Session):
    user = User(login=user.login,
        email = user.email,
        hashed_password=encrypt_password(user.hashed_password)
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user