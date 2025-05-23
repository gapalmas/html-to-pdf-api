from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="HTML to PDF API")

app.include_router(router, prefix="/api")
