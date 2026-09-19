from typing import Literal, Optional
from datetime import datetime, timezone
from pydantic import BaseModel, Field

class RawLeadWebhook(BaseModel):
    lead_name: str = Field(..., description="Name of the lead or primary contact")
    contact_email: str = Field(..., description="Email address for lead contact")
    account_id: str = Field(..., description="Unique client account identifier")
    raw_notes: str = Field(..., description="Unstructured lead request text or emergency submission notes")
    timestamp: Optional[str] = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    request_id: Optional[str] = Field(default=None, description="Inbound webhook tracking ID")

class LeadTriageResponse(BaseModel):
    lead_name: str
    urgency_level: Literal["HIGH", "MEDIUM", "LOW"]
    category: str
    action_summary: str
    processed_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
