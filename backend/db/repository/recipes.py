from sqlalchemy.orm import Session
from backend.schemas.recipes import RecipeCreate
from backend.db.models import Recipe
from sqlalchemy.exc import IntegrityError
from sqlalchemy import exc
from fastapi import HTTPException


def create_new_recipe(recipe: RecipeCreate,db: Session,user_id:int):
    existing_tag = db.query(Recipe).filter_by(name=recipe.name).first()
    if existing_tag:
        raise HTTPException(status_code=409, detail="Recipe with the same name already exists")
    try:
        recipe_object = Recipe(**recipe.dict(), user_id=user_id)
        db.add(recipe_object)
        db.commit()
        db.refresh(recipe_object)
        return recipe_object
    except exc.SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")
def get_all_recipes(db: Session):
    all_recipes = db.query(Recipe).all()
    return all_recipes

def get_recipe_id(db: Session, id: int):
    recipe = db.query(Recipe).filter(Recipe.id == id).first()
    return recipe