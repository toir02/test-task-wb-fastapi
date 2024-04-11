from fastapi import FastAPI

from app import app_router

app = FastAPI()

app.include_router(app_router)
