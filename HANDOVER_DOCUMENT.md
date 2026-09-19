# Client Handoff & Production Support SOP
**Author:** Ajay Meena | Forward Deployed Engineering Masterclass  
**System:** Hardened HealthPulse Client Agent  
**Client:** HealthPulse Technologies (Digital Health Platform)  

---

## 1. Executive Summary
Deployed a 2-stage security hardening layer for the HealthPulse Technologies internal support agent. The solution intercepts user queries before downstream model execution to redact sensitive patient PII (SSNs, emails, phone numbers) and block prompt injection attacks (`system override`, `ignore previous instructions`, `reveal key`). All query processing and security interventions are recorded in structured UTC audit logs.

---

## 2. Environment Setup & Configuration
Required environment variables (`.env` file):

```env
LLM_API_KEY="your-api-key-here"
LOG_LEVEL="INFO"
```

### Installation & Quick Start
1. Create virtual environment:
   ```bash
   py -3.12 -m venv venv
   ```
2. Install dependencies:
   ```bash
   .\venv\Scripts\python -m pip install -r requirements.txt
   ```
3. Run hardened agent:
   ```bash
   .\venv\Scripts\python src/agent.py
   ```
4. Run security test suite:
   ```bash
   .\venv\Scripts\python -m unittest src.test_vulnerabilities
   ```

---

## 3. Security Guardrails & Middleware Architecture
- `src/guardrails.py`: Fast pattern-matching engine containing:
  - `sanitize_pii(text: str) -> str`: Replaces SSNs (`\d{3}-\d{2}-\d{4}`), emails, and phone numbers with `[REDACTED_SSN]`, `[REDACTED_EMAIL]`, and `[REDACTED_PHONE]`.
  - `detect_prompt_injection(text: str) -> bool`: Identifies prompt override signatures and short-circuits execution.
- `src/agent.py`: Intercepts queries, triggers `[SECURITY_ALERT]` for injection attempts, applies `sanitize_pii()` before dispatch, and writes UTC timestamped audit events.
- `src/test_vulnerabilities.py`: `unittest` suite asserting PII redaction and prompt injection blocking.

---

## 4. Operational Runbook & Support
- **Prompt Injection Defense**: Suspicious inputs trigger an immediate return string `"Security Alert: Request blocked."` with a `[SECURITY_ALERT]` warning logged.
- **Audit Compliance**: All inbound requests log UTC timestamps and sanitized text for compliance auditing.
