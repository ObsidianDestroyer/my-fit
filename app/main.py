from fastapi.applications import FastAPI

from app.server import app_factory


app: FastAPI = app_factory()
