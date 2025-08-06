from fastapi.routing import APIRouter

from app.application.api.meals import meals_router

root_router = APIRouter(prefix='/api')
root_router.include_router(meals_router)
