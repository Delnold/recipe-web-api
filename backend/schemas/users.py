from typing import Optional
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    login: str
    email : EmailStr
    hashed_password : str
    class Config():
        orm_mode = True
class UserAdditional(BaseModel):
    biography: str
    class Config():
        orm_mode = True