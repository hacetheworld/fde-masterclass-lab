# Client Handoff & Production Support SOP
**Author:** Ajay Meena | Forward Deployed Engineering Masterclass  
**System:** FinFlow Lead Triage Automation Service  
**Client:** FinFlow Solutions (B2B SaaS / Fintech)  

---

## 1. Executive Summary
Deployed an automated B2B lead triage and routing pipeline for FinFlow Solutions. The service ingests raw webhook customer payloads from marketing forms, parses unstructured emergency notes into a validated Pydantic schema (`LeadTriageSchema`), classifies operational urgency (`HIGH`, `MEDIUM`, `LOW`), extracts actionable summaries, and triggers high-priority alert dispatches (simulated webhook/Slack alerts) for critical $250k production drawdown emergencies.

---

## 2. Environment Setup & Configuration
Required environment variables (`.env` file):

```env
LLM_API_KEY="your-api-key-here"
ALERT_WEBHOOK_URL="https://httpbin.org/post"
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
3. Run lead triage service:
   ```bash
   .\venv\Scripts\python src/app.py
   ```
4. Run test suite:
   ```bash
   .\venv\Scripts\python -m unittest src.test_app
   ```

---

## 3. Architecture & File Inventory
- `src/app.py`: Core ingestion pipeline, Pydantic schema validation, urgency classification, and webhook dispatch logic.
- `src/test_payload.json`: Sample raw B2B lead payload containing high-urgency drawdown emergency notes.
- `src/test_app.py`: Unit test suite verifying schema validation and high-urgency alert pathways.
- `requirements.txt`: Lightweight production dependencies (`pydantic`, `python-dotenv`).

---

## 4. Operational Runbook & Support
- **High-Urgency Alert Handling**: When `urgency_level == "HIGH"`, a structured log `[HIGH URGENCY ALERT]` is outputted and an HTTP POST is dispatched to `ALERT_WEBHOOK_URL`.
- **Error Handling**: Missing required fields or malformed JSON payloads trigger explicit validation errors logged with stack traces.
