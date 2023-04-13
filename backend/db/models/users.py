from sqlalchemy import Column, ForeignKey, Integer, Table, Text, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import NullType
from backend.db.base_class import Base


class User(Base):
    __tablename__ = 'user_sql_alchemy'

    id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    biography = Column(Text, nullable = False)
    recipe = relationship('Recipe')