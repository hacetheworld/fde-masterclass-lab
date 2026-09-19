from datetime import datetime, timezone
from pydantic import BaseModel, Field

class AgentQueryRequest(BaseModel):
    user_id: str = Field(..., description="Unique client or patient user identifier")
    query: str = Field(..., description="Raw incoming user or patient query text")

class AgentQueryResponse(BaseModel):
    user_id: str
    sanitized_query: str
    response: str
    security_flagged: bool
    processed_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
