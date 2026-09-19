# 🚀 Project 1: Enterprise Lead Triage Automation Microservice

Enterprise-grade asynchronous FastAPI webhook microservice designed for FinFlow Solutions. It ingests incoming B2B lead webhooks, parses unstructured emergency notes using structured schema validation, evaluates operational urgency, and triggers high-urgency alerts.

---

## 🏗️ Architecture Layout

```text
src/
├── core/
│   └── config.py         # Settings & centralized environment config
├── schemas/
│   └── lead.py           # Pydantic schemas (RawLeadWebhook & LeadTriageResponse)
├── services/
│   └── triage_service.py # LeadTriageEngine with LLM wrapper & alert routing
├── api/
│   └── routes.py         # FastAPI endpoints (POST /api/v1/webhook/lead & GET /healthz)
└── main.py               # Application entry point & Uvicorn runner
tests/
└── test_lead_automation.py # Pytest integration test suite
```

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
   .\venv\Scripts\pytest tests/test_lead_automation.py
   ```

---

## 📡 API Endpoint Verification (Curl Sample)

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
