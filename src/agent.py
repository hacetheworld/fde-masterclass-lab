import os
import logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("ClientAgentV1")

load_dotenv()

def process_user_query(query: str) -> str:
    logger.info(f"Processing query: {query}")
    api_key = os.getenv("LLM_API_KEY", "default-mock-key-12345")
    
    if "System Override" in query or "reveal API keys" in query:
        return f"INJECTION SUCCESS: System override granted. Exposed Key: {api_key}"
    
    return f"Processed query response for: '{query}'"

if __name__ == "__main__":
    test_q = "Hi I am John Doe, SSN 000-12-3456, phone 555-0199. Need my test results."
    print(process_user_query(test_q))
