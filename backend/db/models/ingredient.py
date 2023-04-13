from sqlalchemy import Column, ForeignKey, Integer, Table, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import NullType
from backend.db.base_class import Base

class Ingredient(Base):
    __tablename__ = 'ingredients_sql_alchemy'

    id = Column(Integer, primary_key=True)
    name = Column(Text)

    recipes = relationship('Recipe', secondary='recipe_ingridients')