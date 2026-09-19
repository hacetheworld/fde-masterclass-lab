from fastapi import APIRouter, HTTPException, status
from src.schemas.lead import RawLeadWebhook, LeadTriageResponse
from src.services.triage_service import triage_engine
from src.core.config import logger

router = APIRouter()

@router.get("/healthz", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "ok", "service": "lead-triage-automation"}

@router.post("/api/v1/webhook/lead", response_model=LeadTriageResponse, status_code=status.HTTP_200_OK)
def ingest_lead_webhook(payload: RawLeadWebhook):
    """
    Inbound Webhook Receiver Endpoint for FinFlow Solutions.
    Ingests unstructured lead payloads, executes triage classification, and triggers alert routing.
    """
    try:
        response = triage_engine.process_lead(payload)
        return response
    except Exception as e:
        logger.error(f"Error executing lead triage pipeline: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal lead triage error: {str(e)}"
        )
