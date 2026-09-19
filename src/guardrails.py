import re

SSN_PATTERN = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
EMAIL_PATTERN = re.compile(r"[\w\.-]+@[\w\.-]+\.\w+")
PHONE_PATTERN = re.compile(r"\b\d{3}-\d{3}-\d{4}\b|\b555-\d{4}\b|\b\d{10}\b")

INJECTION_KEYWORDS = [
    "ignore previous",
    "ignore all previous",
    "system override",
    "reveal api key",
    "reveal key",
    "bypass guardrail"
]

def sanitize_pii(text: str) -> str:
    scrubbed = SSN_PATTERN.sub("[REDACTED_SSN]", text)
    scrubbed = EMAIL_PATTERN.sub("[REDACTED_EMAIL]", scrubbed)
    scrubbed = PHONE_PATTERN.sub("[REDACTED_PHONE]", scrubbed)
    return scrubbed

def detect_prompt_injection(text: str) -> bool:
    lowered = text.lower()
    return any(kw in lowered for kw in INJECTION_KEYWORDS)
