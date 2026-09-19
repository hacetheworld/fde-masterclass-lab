import os
import logging
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PORT: int = int(os.getenv("PORT", "8000"))
    LLM_API_KEY: str = os.getenv("LLM_API_KEY", "")
    WEBHOOK_SECRET: str = os.getenv("WEBHOOK_SECRET", "default-webhook-secret")
    ALERT_URL: str = os.getenv("ALERT_URL", "https://httpbin.org/post")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()

logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO),
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s"
)
logger = logging.getLogger("FinFlowLeadTriage")
