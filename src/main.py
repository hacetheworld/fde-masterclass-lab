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
    logger.info(f"HealthPulse Hardened Support Agent initialized on port {settings.PORT}")
    yield
    logger.info("Shutting down HealthPulse Hardened Support Agent")

app = FastAPI(
    title="HealthPulse Hardened Support Agent API",
    description="3-Tier Security Hardened AI Agent Microservice with PII Redaction & Prompt Injection Shield",
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
