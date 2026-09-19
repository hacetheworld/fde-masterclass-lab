import sys
import os
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.main import app

client = TestClient(app)

def test_healthz():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "lead-triage-automation"}

def test_high_urgency_webhook_flow():
    payload = {
        "lead_name": "John Sterling",
        "contact_email": "john.sterling@acme-corp.com",
        "account_id": "ACC-98421",
        "raw_notes": "URGENT: We are facing a $250k production drawdown emergency on server cluster B. Systems are down!",
        "request_id": "REQ-100293"
    }
    response = client.post("/api/v1/webhook/lead", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["lead_name"] == "John Sterling"
    assert data["urgency_level"] == "HIGH"
    assert data["category"] == "VIP_EMERGENCY"
    assert "processed_at" in data

def test_malformed_payload():
    invalid_payload = {
        "contact_email": "john.sterling@acme-corp.com",
        "raw_notes": "Emergency!"
    }
    response = client.post("/api/v1/webhook/lead", json=invalid_payload)
    assert response.status_code == 422
