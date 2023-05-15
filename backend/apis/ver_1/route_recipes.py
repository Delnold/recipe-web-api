from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status

from backend.db.session import get_db
from backend.schemas.recipes import RecipeCreate,RecipeView
from backend.db.repository.recipes import create_new_recipe, get_all_recipes, get_recipe_id

router = APIRouter()


@router.post("/create/",response_model=RecipeView)
def create_recipe(recipe: RecipeCreate,db: Session = Depends(get_db)):
    try:
        current_user = 1
        recipe = create_new_recipe(recipe=recipe,db=db, user_id=current_user)
        return recipe
    finally:
        pass

@router.get("/all/")
def get_recipes(db: Session = Depends(get_db)):
    recipe = get_all_recipes(db=db)
    if recipe is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")
    return recipe
@router.get("/get/{id}", response_model=RecipeView)
def get_recipe_by_id(id: int, db: Session = Depends(get_db)):
    recipe = get_recipe_id(db=db, id=id)
    if recipe is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")
    return recipe