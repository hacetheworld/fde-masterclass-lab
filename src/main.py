import os
import sys
from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.api.routes import router
from src.core.config import settings, logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"FinFlow Lead Triage Service initialized on port {settings.PORT}")
    yield
    logger.info("Shutting down FinFlow Lead Triage Service")

app = FastAPI(
    title="FinFlow Lead Triage API",
    description="Automated Enterprise B2B Lead Ingestion, Triage & Alert Dispatch Service",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=settings.PORT, reload=True)
