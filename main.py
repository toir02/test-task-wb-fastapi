from fastapi import FastAPI

from app.routes import app_router

app = FastAPI()

app.include_router(app_router)
