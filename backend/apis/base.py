from fastapi import APIRouter
from .ver_1 import route_general_pages
from .ver_1 import route_users
from .ver_1 import route_recipes
from .ver_1 import route_tags

api_router = APIRouter()
api_router.include_router(route_general_pages.general_pages_router,prefix="",tags=["general_pages"])
api_router.include_router(route_recipes.router,prefix="/recipes",tags=["recipes"])
api_router.include_router(route_tags.router, prefix="/tags", tags=["tags"])

"""

For the future...
api_router.include_router(route_users.router,prefix="/users",tags=["users"])

"""