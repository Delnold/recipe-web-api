from typing import Optional
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    login: str
    email : EmailStr
    hashed_password : str
class UserExtended(BaseModel):
    biography: str