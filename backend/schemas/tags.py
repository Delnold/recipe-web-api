from pydantic import BaseModel

class TagCreate(BaseModel):
    name: str
    description: str
    class Config():
        orm_mode = True
class TagView(BaseModel):
    name: str
    description: str
    class Config():
        orm_mode = True