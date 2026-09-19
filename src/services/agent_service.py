from datetime import datetime, timezone
from src.core.config import settings, logger
from src.core.security import sanitize_pii, detect_prompt_injection
from src.schemas.agent import AgentQueryRequest, AgentQueryResponse

class SecureAgentService:
    """
    3-Tier Hardened AI Agent Service powering HealthPulse support endpoint.
    Pipeline:
      1. Pre-execution Security Check (Prompt Injection Shield) + UTC Audit Event Logging.
      2. Input PII Sanitization (SSN, Email, Phone Redaction).
      3. Secure LLM Execution Layer.
    """

    def _call_llm_agent(self, sanitized_query: str) -> str:
        """
        Secure LLM Model Provider Hook.
        
        PRODUCTION EXTENSION HOOK:
        To integrate live LangChain, LlamaIndex, or OpenAI agent pipelines, replace mock logic:
            agent_executor = create_langchain_agent(model="gpt-4o")
            return agent_executor.invoke({"input": sanitized_query})["output"]
        """
        return f"Processed query response for: '{sanitized_query}'"

    def process_query(self, payload: AgentQueryRequest) -> AgentQueryResponse:
        timestamp = datetime.now(timezone.utc).isoformat()
        logger.info(f"[{timestamp}] [AUDIT_LOG] User '{payload.user_id}' submitted a support query.")

        if detect_prompt_injection(payload.query):
            logger.warning(
                f"[{timestamp}] [SECURITY_AUDIT_LOG] PROMPT INJECTION BLOCKED for User '{payload.user_id}'. "
                f"Raw Query snippet: {payload.query[:60]}..."
            )
            return AgentQueryResponse(
                user_id=payload.user_id,
                sanitized_query=payload.query,
                response="Security Alert: Request blocked by safety guardrails.",
                security_flagged=True,
                processed_at=timestamp
            )

        sanitized_text = sanitize_pii(payload.query)
        logger.info(f"[{timestamp}] [AUDIT_LOG] Query scrubbed successfully for User '{payload.user_id}': {sanitized_text}")

        model_response = self._call_llm_agent(sanitized_text)

        return AgentQueryResponse(
            user_id=payload.user_id,
            sanitized_query=sanitized_text,
            response=model_response,
            security_flagged=False,
            processed_at=timestamp
        )

secure_agent_service = SecureAgentService()
