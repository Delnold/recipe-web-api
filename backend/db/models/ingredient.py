from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from backend.db.base_class import Base

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(Text)

class RecipeIngredient(Base):
    __tablename__ = "recipes_ingredients"
    recipe_id = Column(Integer, ForeignKey("recipes.id"), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"), primary_key=True)
    recipe = relationship("Recipe")
    ingredient = relationship("Ingredient")
