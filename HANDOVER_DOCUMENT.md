# Client Handoff & Production Support SOP
**Author:** Ajay Meena | Forward Deployed Engineering Masterclass  
**System:** Hardened HealthPulse Support Agent Microservice  
**Client:** HealthPulse Technologies (Digital Health Platform)  

---

## 1. Executive Summary
Deployed a 3-tier production-grade security microservice powered by FastAPI and Uvicorn for HealthPulse Technologies. The service exposes a secure chat endpoint at `POST /api/v1/agent/chat` that intercepts user/patient queries, redacts sensitive PII (SSNs, emails, phone numbers) before model execution, blocks prompt injection attacks (`system override`, `ignore previous instructions`, `reveal key`), and records structured UTC compliance audit logs. Includes health check endpoint (`GET /healthz`).

---

## 2. Environment Setup & Configuration
Required environment variables (`.env` file):

```env
PORT=8000
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
3. Run production FastAPI server:
   ```bash
   py -3.12 src/main.py
   # OR: .\venv\Scripts\python -m uvicorn src.main:app --reload --port 8000
   ```
4. Run Pytest security test suite:
   ```bash
   .\venv\Scripts\pytest tests/test_agent_security.py
   ```

---

## 3. Architecture & File Inventory
- `src/main.py`: Application entry point with Uvicorn server launcher, lifespan handlers, and CORS middleware.
- `src/api/routes.py`: FastAPI routes for `POST /api/v1/agent/chat` and `GET /healthz`.
- `src/schemas/agent.py`: Pydantic request (`AgentQueryRequest`) and response (`AgentQueryResponse`) models.
- `src/services/agent_service.py`: `SecureAgentService` 3-tier pipeline executing pre-execution prompt injection check + `[SECURITY_AUDIT_LOG]`, PII redaction, and model context provider hooks.
- `src/core/security.py`: Guardrail engine featuring regex PII scrubber (`sanitize_pii`) and prompt injection shield (`detect_prompt_injection`).
- `src/core/config.py`: Centralized environment configuration and structured logging setup.
- `tests/test_agent_security.py`: Pytest suite verifying PII redaction (`[REDACTED_SSN]`, `[REDACTED_PHONE]`), prompt injection defense (`security_flagged: True`), and health check.
- `requirements.txt`: Dependencies (`fastapi`, `uvicorn`, `pydantic`, `python-dotenv`, `pytest`, `httpx`).

---

## 4. Operational Runbook & Support
- **Verification via Curl**:
  ```bash
  curl -X POST "http://localhost:8000/api/v1/agent/chat" \
       -H "Content-Type: application/json" \
       -d '{
         "user_id": "PATIENT-99021",
         "query": "Hi I am John Doe, SSN 000-12-3456, phone 555-0199. Need my test results."
       }'
  ```
- **Prompt Injection Shield**: Suspicious queries are flagged (`security_flagged: true`), returned with `"Security Alert: Request blocked by safety guardrails."`, and logged to UTC security audit logs.
- **Health Monitoring**: `GET /healthz` returns `{"status": "ok", "service": "hardened-client-agent"}`.
