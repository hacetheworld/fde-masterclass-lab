# Client Discovery & Requirements SOP
**Author:** Ajay Meena | Forward Deployed Engineering Masterclass

> **Rule of FDE:** Never start coding on Day 1. Ask strategic questions first to uncover hidden assumptions, guard against scope creep, and build client trust.

---

## Phase 1: Business Context & Pain Point
Do not accept vague prompts like *"We want an AI agent to handle support."* Get specific metrics and target outcomes.

- [ ] **What is the current manual process?** 
  - *Context:* How many human hours or manual steps does this task take today?
- [ ] **What is the definition of success?** 
  - *Context:* Is success 90% automation, 2x faster response time, or zero PII leakage?
- [ ] **What fails if this tool is offline for 2 hours?**
  - *Context:* This determines whether you need hard fallbacks (e.g., human routing) or simple retry queues.

---

## Phase 2: Technical & Data Boundaries
Clients often assume an LLM can magically access internal DBs or third-party APIs without credentials.

- [ ] **Data Source Locations:** Where does the ground-truth data live? (e.g., Postgres, Notion, Zendesk API, static PDFs)
- [ ] **Environment & Credentials:** Do we have dedicated sandbox/staging API keys, or are we testing against live production endpoints?
- [ ] **Rate Limits & Budgets:** What is the monthly token budget cap or vendor API limit?

---

## Phase 3: Security & Compliance Checklist
- [ ] **PII Handling:** Will this agent process names, emails, phone numbers, or payment data?
- [ ] **Untrusted Input Sources:** Can end users send raw text directly to the prompt? (High risk for prompt injection).
- [ ] **Access Control (RBAC):** Does the agent perform actions (e.g., database writes, sending emails) that require specific user permission checks?