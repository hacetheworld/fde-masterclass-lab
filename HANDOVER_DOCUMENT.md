# Client Handoff & Production Support SOP
**Author:** Ajay Meena | Forward Deployed Engineering Masterclass  
**System:** FinFlow Enterprise Lead Triage Microservice  
**Client:** FinFlow Solutions (B2B SaaS / Fintech)  

---

## 1. Executive Summary
Deployed an asynchronous, enterprise-grade FastAPI lead triage microservice for FinFlow Solutions. The microservice ingests incoming B2B marketing lead webhooks at `POST /api/v1/webhook/lead`, parses unstructured customer notes using strict Pydantic schemas (`RawLeadWebhook` -> `LeadTriageResponse`), classifies operational urgency (`HIGH`, `MEDIUM`, `LOW`), extracts actionable summaries, and dispatches real-time high-urgency notifications for critical $250k production drawdown emergencies. Includes standard health check endpoint (`GET /healthz`).

---

## 2. Environment Setup & Configuration
Required environment variables (`.env` file):

```env
PORT=8000
LLM_API_KEY="your-api-key-here"
WEBHOOK_SECRET="your-webhook-secret-here"
ALERT_URL="https://httpbin.org/post"
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
4. Run Pytest integration test suite:
   ```bash
   .\venv\Scripts\pytest tests/test_lead_automation.py
   ```

---

## 3. Architecture & File Inventory
- `src/main.py`: Application entry point with Uvicorn server launcher, lifespan handlers, and CORS middleware.
- `src/api/routes.py`: FastAPI routes for `POST /api/v1/webhook/lead` and `GET /healthz`.
- `src/schemas/lead.py`: Pydantic request (`RawLeadWebhook`) and response (`LeadTriageResponse`) models.
- `src/services/triage_service.py`: `LeadTriageEngine` featuring `_call_llm_classifier()` (with OpenAI/Anthropic provider hooks), `_dispatch_high_urgency_alert()`, and `process_lead()`.
- `src/core/config.py`: Environment configuration and structured logging setup.
- `tests/test_lead_automation.py`: Pytest suite testing health check, webhook ingestion, high-urgency alert dispatch, and 422 error handling.
- `requirements.txt`: Dependencies (`fastapi`, `uvicorn`, `pydantic`, `python-dotenv`, `pytest`, `httpx`).

---

## 4. Operational Runbook & Support
- **Verification via Curl**:
  ```bash
  curl -X POST "http://localhost:8000/api/v1/webhook/lead" \
       -H "Content-Type: application/json" \
       -d '{
         "lead_name": "John Sterling",
         "contact_email": "john.sterling@acme-corp.com",
         "account_id": "ACC-98421",
         "raw_notes": "URGENT: Facing a $250k production drawdown emergency!",
         "request_id": "REQ-99218"
       }'
  ```
- **High-Urgency Alerts**: Dispatched automatically to `ALERT_URL` when `urgency_level == "HIGH"`.
- **Health Monitoring**: `GET /healthz` returns `{"status": "ok", "service": "lead-triage-automation"}`.
