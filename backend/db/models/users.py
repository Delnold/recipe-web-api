from sqlalchemy import Column, Integer, Text, String
from sqlalchemy.orm import relationship
from backend.db.base_class import Base


class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True)
        login = Column(String, nullable=False, unique = True)
        hashed_password = Column(String, nullable=False)
        email = Column(String, nullable=False)
        biography = Column(Text, nullable = True)
        recipe = relationship('Recipe')
