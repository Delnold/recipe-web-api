from pydantic import root_validator
from pydantic import BaseModel

class RecipeCreate(BaseModel):
    name: str
    description: str
    instructions: str
    prep_time: int
    cook_time: int
    servings: str
    class Config():
        orm_mode = True

    @root_validator
    def calculate_total_time(cls, values):
        values['total_time'] = values['prep_time'] + values['cook_time']
        return values

class RecipeView(BaseModel):
    name: str
    description: str
    instructions: str
    prep_time: int
    cook_time: int
    servings: str
    total_time: int
    class Config():
        orm_mode = True