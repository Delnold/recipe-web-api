from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.db.base_class import Base

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    recipe = relationship('Recipe')

