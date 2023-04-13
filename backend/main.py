from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from apis.general_pages.route_homepage import general_pages_router
from backend.db.base_class import Base
from db.session import engine
from db.base import Base

def configure_static(application):
	application.mount("/static", StaticFiles(directory="static"), name="static")

def include_router(application):
	application.include_router(general_pages_router)

def create_tables():
	Base.metadata.create_all(bind=engine)
def start_application():
	application = FastAPI()
	include_router(application)
	create_tables()
	return application




app = start_application()

