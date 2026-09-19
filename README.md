# 🛡️ Project 2: Hardened AI Support Agent Microservice

Production-grade 3-tier security microservice powering the HealthPulse Technologies support agent. Built with FastAPI and Uvicorn, featuring PII sanitization middleware, adversarial prompt injection shields, and UTC audit event logging.

---

## 🏗️ Architecture Layout

```text
src/
├── core/
│   ├── config.py         # Settings & environment configuration
│   └── security.py       # PII Redactor (sanitize_pii) & Prompt Injection Shield (detect_prompt_injection)
├── schemas/
│   └── agent.py          # Pydantic schemas (AgentQueryRequest & AgentQueryResponse)
├── services/
│   └── agent_service.py  # SecureAgentService pipeline & LLM provider hooks
├── api/
│   └── routes.py         # FastAPI endpoints (POST /api/v1/agent/chat & GET /healthz)
└── main.py               # Application entry point & Uvicorn runner
tests/
└── test_agent_security.py # Pytest integration test suite
```

---

## 🔒 3-Tier Security Middleware Pipeline

1. **Pre-Execution Injection Shield**: Inspects input queries against prompt injection, jailbreak, and key extraction vectors. Suspicious queries short-circuit execution, return a security alert block, and log a `[SECURITY_AUDIT_LOG]` warning.
2. **Input PII Sanitization**: Replaces sensitive SSNs (`\d{3}-\d{2}-\d{4}`), emails, and phone numbers with `[REDACTED_SSN]`, `[REDACTED_EMAIL]`, and `[REDACTED_PHONE]` before LLM execution.
3. **UTC Audit Logging**: All inbound requests and security flags record UTC ISO timestamps for regulatory compliance.

---

## ⚡ Quick Start & Execution

1. **Environment Setup**:
   ```bash
   py -3.12 -m venv venv
   .\venv\Scripts\python -m pip install -r requirements.txt
   ```

2. **Configure Environment**:
   ```bash
   cp .env.example .env
   ```

3. **Run Production Server**:
   ```bash
   .\venv\Scripts\python -m uvicorn src.main:app --reload --port 8000
   ```

4. **Run Integration Test Suite**:
   ```bash
   .\venv\Scripts\pytest tests/test_agent_security.py
   ```

---

## 📡 API Endpoint Verification (Curl Sample)

```bash
curl -X POST "http://localhost:8000/api/v1/agent/chat" \
     -H "Content-Type: application/json" \
     -d '{
       "user_id": "PATIENT-99021",
       "query": "Hi I am John Doe, SSN 000-12-3456, phone 555-0199. Need my test results."
     }'
```
