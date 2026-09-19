# Client Requirement: Zero-to-One Lead Triage & Action Automation
**Instructor / Lead FDE:** Ajay Meena  
**Client:** FinFlow Solutions (B2B SaaS / Fintech)

---

## 1. Background & The Real-World Chaos
FinFlow Solutions runs a growing platform for small business credit lines. Over the last 6 months, their incoming contact volume exploded from 5 submissions a day to over 80+. 

Every inbound lead comes through a single raw "Contact Us" form on their marketing site. The form dumps raw JSON payloads via a generic webhook into an internal database.

Here is what happens every morning at 8:00 AM:
1. Sarah, the Lead Customer Success Manager, opens a massive database table containing 80+ unorganized, raw text entries.
2. She spends **2.5 to 3 hours manually reading** every single entry.
3. She manually categorizes urgency:
   - Is it a VIP enterprise client with an active pipeline emergency? (**HIGH Urgency**)
   - Is it a general billing question or account query? (**MEDIUM Urgency**)
   - Is it someone asking for a link to pricing or selling spam services? (**LOW Urgency**)
4. She copy-pastes extracted summary notes into Slack channels and sends emails to designated account managers.

### The Problem:
Last Tuesday, a $250,000 credit line applicant submitted a urgent message saying their drawdown was failing on production. Because the submission sat in Sarah’s manual review queue until 11:30 AM, the prospect abandoned FinFlow and signed with a competitor. 

The CEO called an emergency meeting and declared: *"We don't need a massive customer portal overhaul right now. We need an automated system in place by Friday that ingests this raw webhook, classifies the urgency, extracts the key action item, and routes it cleanly."*

---

## 2. What the Client Thinks They Want vs. What the FDE Builds

* **Client's Naive Request:** *"Build us a massive microservice with a full dashboard, user management, and custom database tables for lead management."*
* **The FDE Approach:** Build a lightweight, bulletproof webhook ingestion script in Python that uses a single LLM call to structure messy incoming text into a strict JSON payload, assigns priority, and prints/logs the structured action item. Fast to build, zero bloat, deployed in hours.

---

## 3. Scope of Engineering Work

Your objective in this branch is to take the raw webhook payload in `test_payload.json` and build a lightweight parser (`app.py`) that executes the following pipeline:

1. **Webhook Ingestion:** Accept raw webhook JSON containing unstructured customer text.
2. **LLM Extraction & Classification:** Pass the raw text through an LLM call enforcing a strict JSON schema:
   - `lead_name` (string)
   - `urgency_level` (`HIGH` | `MEDIUM` | `LOW`)
   - `category` (`VIP_EMERGENCY` | `BILLING` | `GENERAL` | `SPAM`)
   - `action_summary` (1-sentence summary of what needs to be done)
3. **Deterministic Routing:** If `urgency_level == "HIGH"`, immediately trigger a simulated high-priority alert (e.g., console alert or Slack webhook format).

---

## 4. Definition of Done (FDE Verification)
- [ ] Running `python app.py` ingests the sample messy payload without crashing.
- [ ] Output is clean, validated JSON adhering to the required schema.
- [ ] High-urgency leads trigger the alert pathway cleanly.
- [ ] The `HANDOVER_DOCUMENT_TEMPLATE.md` is populated with setup instructions for the client team.