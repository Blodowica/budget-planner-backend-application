from fastapi import FastAPI

from app.config import settings
from app.controllers import example

app = FastAPI(title=settings.app_name)

app.include_router(example.router)


@app.get("/")
def root():
    return {"message": "Budget Planner API is running"}
