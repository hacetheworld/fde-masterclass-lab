# Project 2 (Production): Hardened Client Agent

Production-grade security middleware protecting AI client agents against PII leakage and prompt injection vectors.

## Implemented Guardrails & Security Controls

1. **PII Sanitization Middleware (`guardrails.py`)**:
   - `sanitize_pii(text: str)` automatically scrubs sensitive fields including SSNs (`\d{3}-\d{2}-\d{4}`), emails, and phone numbers before user queries are dispatched to LLM endpoints. Replaces matching tokens with `[REDACTED_SSN]`, `[REDACTED_EMAIL]`, and `[REDACTED_PHONE]`.

2. **Prompt Injection Shield (`guardrails.py`)**:
   - `detect_prompt_injection(text: str)` inspects input strings for override phrases (e.g. `system override`, `ignore previous`, `reveal key`). Requests matching injection signatures trigger a `[SECURITY_ALERT]` and return a sanitized security block response without executing downstream logic.

3. **Security Audit Logging (`agent.py`)**:
   - All inbound queries and security events are logged with UTC timestamps for compliance auditing.

## Verification

Run unit test assertions:
```bash
py -3.12 -m unittest src/test_vulnerabilities.py
```
All tests verify PII redaction and injection blocking cleanly.
