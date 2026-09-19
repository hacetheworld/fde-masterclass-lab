from fastapi import APIRouter, HTTPException, status
from src.schemas.agent import AgentQueryRequest, AgentQueryResponse
from src.services.agent_service import secure_agent_service
from src.core.config import logger

router = APIRouter()

@router.get("/healthz", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "ok", "service": "hardened-client-agent"}

@router.post("/api/v1/agent/chat", response_model=AgentQueryResponse, status_code=status.HTTP_200_OK)
def process_agent_chat(payload: AgentQueryRequest):
    """
    Hardened AI Support Agent Endpoint for HealthPulse Technologies.
    Runs inbound user queries through PII scrubbing and prompt injection shields prior to model execution.
    """
    try:
        return secure_agent_service.process_query(payload)
    except Exception as e:
        logger.error(f"Error processing agent query: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Agent service processing error: {str(e)}"
        )
