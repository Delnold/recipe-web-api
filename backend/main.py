from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.apis.base import api_router
from db.session import engine
from db.models import Base

def configure_static(application):
	application.mount("/static", StaticFiles(directory="static"), name="static")

def include_router(application):
	application.include_router(api_router)

def create_tables():
	Base.metadata.create_all(bind=engine)

def start_application():
	application = FastAPI()
	include_router(application)
	create_tables()
	return application




app = start_application()

