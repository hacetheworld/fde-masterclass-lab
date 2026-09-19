# Architectural Decision Record (ADR)
**Author:** Ajay Meena | Forward Deployed Engineering Masterclass  
**Project:** [Insert Project Name]  
**Status:** [Proposed / Accepted / Superseded]

---

## Context & Problem Statement
Briefly describe the business problem, client constraints, and why a standard off-the-shelf feature was insufficient.

---

## Decision Drivers
1. **Speed to Production:** Must be deployable within 48–72 hours.
2. **Security & Guardrails:** Must prevent prompt injection and redact customer PII.
3. **Operational Cost:** Minimal infrastructure overhead and predictable token consumption.

---

## Considered Options
* **Option A:** Heavy custom multi-agent framework with orchestration layers.
* **Option B:** Lightweight single-purpose Python agent with PII middleware + direct webhook hooks.

---

## Chosen Architecture & Justification
**Selected Option:** Option B

### Why:
- **Simplicity & Debuggability:** Single-file execution flow makes error tracing immediate for client teams.
- **Safety First:** Plugs in middleware for input sanitization before hitting model providers.
- **Maintenance Handoff:** Client developers can modify tools without needing to master complex framework abstractions.

---

## Architectural Trade-Offs & Risks
| Choice | Benefit | Trade-Off / Risk | Mitigation |
| :--- | :--- | :--- | :--- |
| Single LLM Call | Low latency & lower cost | Handles complex sub-tasks less flexibly | Fallback to deterministic rules if confidence score is low |
| In-Memory Cache | Fast local execution | Loses state on server restart | Use Redis/Persistent DB for v2 scale |