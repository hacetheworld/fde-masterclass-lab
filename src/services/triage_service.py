import json
import urllib.request
from datetime import datetime, timezone
from src.core.config import settings, logger
from src.schemas.lead import RawLeadWebhook, LeadTriageResponse

class LeadTriageEngine:
    """
    Enterprise Lead Triage Engine responsible for parsing raw incoming lead webhooks,
    classifying operational urgency via LLM or deterministic fallback rules, and
    dispatching real-time high-urgency notifications.
    """

    def _call_llm_classifier(self, lead_name: str, raw_notes: str) -> dict:
        """
        LLM Integration Wrapper for structured Lead Classification.
        
        PRODUCTION EXTENSION HOOK:
        To connect live model providers (OpenAI / Anthropic / Codex), replace mock logic with:
            client = openai.OpenAI(api_key=settings.LLM_API_KEY)
            response = client.beta.chat.completions.parse(
                model="gpt-4o",
                messages=[{"role": "system", "content": "..."}, {"role": "user", "content": raw_notes}],
                response_format=LeadTriageResponse
            )
            return response.choices[0].message.parsed.model_dump()
        """
        notes_upper = raw_notes.upper()
        if any(term in notes_upper for term in ["EMERGENCY", "URGENT", "$250K", "DOWN"]):
            return {
                "urgency_level": "HIGH",
                "category": "VIP_EMERGENCY",
                "action_summary": "Immediate technical lead intervention required for production drawdown failure."
            }
        elif any(term in notes_upper for term in ["WARN", "BILLING", "DEGRADED"]):
            return {
                "urgency_level": "MEDIUM",
                "category": "BILLING",
                "action_summary": "Standard billing escalation queued for account manager review."
            }
        else:
            return {
                "urgency_level": "LOW",
                "category": "GENERAL",
                "action_summary": "Routine lead information request logged."
            }

    def _dispatch_high_urgency_alert(self, triage_data: LeadTriageResponse) -> bool:
        """Simulates an immediate high-urgency alert dispatch to external webhooks or Slack channels."""
        logger.warning(
            f"[HIGH URGENCY ALERT DISPATCH] Priority lead escalation for '{triage_data.lead_name}' "
            f"(Category: {triage_data.category}): {triage_data.action_summary}"
        )
        try:
            payload_bytes = json.dumps(triage_data.model_dump()).encode("utf-8")
            req = urllib.request.Request(
                settings.ALERT_URL,
                data=payload_bytes,
                headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=5) as resp:
                return resp.status in (200, 201, 202)
        except Exception as e:
            logger.error(f"Alert dispatch notification warning: {e}")
            return False

    def process_lead(self, payload: RawLeadWebhook) -> LeadTriageResponse:
        logger.info(f"Processing inbound webhook lead from '{payload.lead_name}' (Account ID: {payload.account_id})")
        
        extracted = self._call_llm_classifier(payload.lead_name, payload.raw_notes)
        
        triage_response = LeadTriageResponse(
            lead_name=payload.lead_name,
            urgency_level=extracted["urgency_level"],
            category=extracted["category"],
            action_summary=extracted["action_summary"],
            processed_at=datetime.now(timezone.utc).isoformat()
        )

        if triage_response.urgency_level == "HIGH":
            self._dispatch_high_urgency_alert(triage_response)

        return triage_response

triage_engine = LeadTriageEngine()
