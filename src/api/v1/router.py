from fastapi import APIRouter

from .endpoints import film, user

api_router = APIRouter()
api_router.include_router(film.router, prefix="/films", tags=["films"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
