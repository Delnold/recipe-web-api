from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.core.config import DATABASE_URL

# engine = create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )
engine = create_engine(
    r"sqlite:///C:\PLProjects\PyProjects\recipe-web-api\backend\recipeDB.db", connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)