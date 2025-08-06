from fastapi.applications import FastAPI

from app.application.api import root_router


def app_factory() -> FastAPI:
    app = FastAPI()
    app.include_router(root_router)
    return app
