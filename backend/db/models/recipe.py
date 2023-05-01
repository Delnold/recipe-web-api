from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from backend.db.base_class import Base



class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text)
    instructions = Column(Text)
    prep_time = Column(Integer)
    cook_time = Column(Integer)
    total_time = Column(Integer)
    servings = Column(Integer)
    tags_id = Column(Integer, ForeignKey("tags.id"))
    user_id = Column(Integer, ForeignKey("users.id"))


