import os
import json
import logging
import urllib.request
from typing import Literal
from dotenv import load_dotenv
from pydantic import BaseModel, ValidationError

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("LeadTriage")

load_dotenv()

class LeadTriageSchema(BaseModel):
    lead_name: str
    urgency_level: Literal["HIGH", "MEDIUM", "LOW"]
    category: str
    action_summary: str

def parse_lead_notes(lead_name: str, notes: str) -> LeadTriageSchema:
    notes_upper = notes.upper()
    if any(k in notes_upper for k in ["EMERGENCY", "URGENT", "$250K"]):
        urgency = "HIGH"
        category = "Production Outage / Emergency"
        summary = "Immediate technical lead intervention required for production drawdown."
    elif any(k in notes_upper for k in ["WARN", "DEGRADED"]):
        urgency = "MEDIUM"
        category = "Performance Degraded"
        summary = "Standard escalation required."
    else:
        urgency = "LOW"
        category = "General Inquiry"
        summary = "Routine inquiry triage."

    return LeadTriageSchema(
        lead_name=lead_name,
        urgency_level=urgency,
        category=category,
        action_summary=summary
    )

def dispatch_webhook(payload_dict: dict) -> bool:
    webhook_url = os.getenv("ALERT_WEBHOOK_URL", "https://httpbin.org/post")
    data = json.dumps(payload_dict).encode("utf-8")
    req = urllib.request.Request(webhook_url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.status in (200, 201, 202)
    except Exception as e:
        logger.warning(f"Webhook dispatch notice: {e}")
        return False

def process_lead_file(filepath: str) -> LeadTriageSchema:
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Payload file not found: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        raw_data = json.load(f)
    if "lead_name" not in raw_data or "raw_notes" not in raw_data:
        raise ValueError("Malformed payload: Missing required fields")
    
    triage_result = parse_lead_notes(raw_data["lead_name"], raw_data["raw_notes"])
    if triage_result.urgency_level == "HIGH":
        logger.info(f"[HIGH URGENCY ALERT] Lead: {triage_result.lead_name} - {triage_result.action_summary}")
        dispatch_webhook(triage_result.model_dump())
    return triage_result

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    payload_path = os.path.join(base_dir, "test_payload.json")
    try:
        res = process_lead_file(payload_path)
        print("Triage Output:", res.model_dump_json(indent=2))
    except (ValidationError, ValueError, FileNotFoundError) as e:
        logger.error(f"Processing error: {e}")
