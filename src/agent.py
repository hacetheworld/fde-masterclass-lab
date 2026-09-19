import os
import logging
from datetime import datetime, timezone
from dotenv import load_dotenv
from guardrails import sanitize_pii, detect_prompt_injection

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("ClientAgentHardened")

load_dotenv()

def process_user_query(query: str) -> str:
    timestamp = datetime.now(timezone.utc).isoformat()
    logger.info(f"[{timestamp}] [AUDIT] Incoming request received")
    
    if detect_prompt_injection(query):
        logger.warning(f"[{timestamp}] [SECURITY_ALERT] Prompt injection blocked!")
        return "Security Alert: Request blocked."
    
    sanitized_query = sanitize_pii(query)
    logger.info(f"[{timestamp}] [AUDIT] Query sanitized successfully: {sanitized_query}")
    
    return f"Processed query response for: '{sanitized_query}'"

if __name__ == "__main__":
    test_q = "Hi I am John Doe, SSN 000-12-3456, phone 555-0199. Need my test results."
    print(process_user_query(test_q))
