import re

SSN_PATTERN = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
EMAIL_PATTERN = re.compile(r"[\w\.-]+@[\w\.-]+\.\w+")
PHONE_PATTERN = re.compile(r"\b\d{3}-\d{3}-\d{4}\b|\b555-\d{4}\b|\b\d{10}\b")

INJECTION_PATTERNS = [
    r"ignore (all )?previous",
    r"system override",
    r"reveal (api )?key",
    r"bypass guardrail",
    r"print system prompt"
]

def sanitize_pii(text: str) -> str:
    """Scrubs sensitive PII tokens (SSNs, emails, phone numbers) replacing them with [REDACTED_*]."""
    scrubbed = SSN_PATTERN.sub("[REDACTED_SSN]", text)
    scrubbed = EMAIL_PATTERN.sub("[REDACTED_EMAIL]", scrubbed)
    scrubbed = PHONE_PATTERN.sub("[REDACTED_PHONE]", scrubbed)
    return scrubbed

def detect_prompt_injection(text: str) -> bool:
    """Detects adversarial system prompt overrides, jailbreaks, and sensitive key extraction attempts."""
    lowered = text.lower()
    return any(re.search(pat, lowered) for pat in INJECTION_PATTERNS)
