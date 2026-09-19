# 🚀 Forward Deployed Engineering (FDE) Masterclass Lab

Welcome to the **FDE Masterclass Lab**! This repository is designed as a hands-on, scenario-driven environment that simulates real-world engineering challenges faced by Forward Deployed Engineers (FDEs) at high-growth tech companies and AI enterprises.

Unlike traditional software engineering courses that focus purely on syntax or algorithmic puzzles, this masterclass teaches you **how to solve ambiguous business problems, interface with clients, design defensive AI systems, and deliver production-ready solutions under real constraints.**

---

## 📖 The FDE Philosophy: Mindset Before Code

As a Forward Deployed Engineer, you operate at the intersection of complex technical architecture and urgent client business needs. You are half high-impact software engineer and half technical strategist. 

This repository demonstrates the core FDE workflow:
1. **Deconstruct the Chaos:** Translate vague, frantic client demands into clear technical specifications (`CLIENT_REQUIREMENT.md`).
2. **Make Trade-Offs Explicit:** Document decisions and architecture choices using standard templates (`DECISION_RECORD_TEMPLATE.md`).
3. **Build Lightweight & Robust Solutions:** Write clean, modular Python code with proper security, environment isolation, error handling, and test coverage.
4. **Harden for Production:** Guard against real-world failures—data leaks, prompt injection attacks, and unhandled API failures.
5. **Ensure Seamless Handovers:** Provide clients with clean, operational handoff materials (`HANDOVER_DOCUMENT_TEMPLATE.md`) and security audit guidelines (`CLIENT_SECURITY_CHECKLIST.md`).

---

## 📂 Repository Structure & Project Branches

The `main` branch serves as the operational hub containing shared engineering templates and standards. Each practical project in this course lives in its own dedicated feature branch, simulating real client engagements.

```text
fde-masterclass-lab/ (main)
├── CLIENT_SECURITY_CHECKLIST.md   # Security baseline for client deployments
├── DECISION_RECORD_TEMPLATE.md     # Architectural Decision Records (ADR)
├── HANDOVER_DOCUMENT_TEMPLATE.md   # Client technical handoff template
└── README.md                       # Master course overview (this file)

```

---

## 🧪 Included Client Scenarios (Branches)

### 🛠️ Scenario 1: Zero-to-One Lead Triage & Action Automation

* **Branch:** `feat/automation-zero-to-one`
* **Client:** *FinFlow Solutions (B2B Fintech)*
* **The Problem:** Incoming inbound leads from a raw marketing webhook sit in a manual queue for hours, causing high-value prospective clients to abandon the product.
* **The FDE Deliverable:** A lightweight, deterministic webhook parsing pipeline that ingests unstructured payloads, applies LLM classification/summarization with strict schemas, and routes high-urgency alerts in real time.
* **Key Skills:** Structured JSON schema extraction, deterministic routing, error handling, and unit testing.

---

### 🛡️ Scenario 2: Auditing & Hardening a Vulnerable Support Agent

* **Branches:**
* `feat/hardening-client-agent` *(V1 Prototype / Vulnerable baseline)*
* `feat/hardening-client-agent-solution` *(V2 Production Hardened)*


* **Client:** *HealthPulse Technologies (Digital Health)*
* **The Problem:** An internal prototype AI support bot leaks customer PII (SSNs, phone numbers, emails) over third-party APIs and is susceptible to system prompt overrides and prompt injection attacks.
* **The FDE Deliverable:** A 2-stage defensive middleware layer (`guardrails.py`) that redacts PII using pattern-matching regex and intercepts prompt injection vectors before they reach the model provider, complete with security audit logging.
* **Key Skills:** Input sanitization middleware, defensive prompt engineering, PII redaction, security event logging, and adversarial testing.

---

## 🚦 How to Work Through This Workshop

1. **Explore the Root Checklists:** Review `CLIENT_SECURITY_CHECKLIST.md` and the templates to understand how professional technical handoffs are structured.
2. **Switch to a Feature Branch:**
```bash
git checkout feat/automation-zero-to-one
# OR
git checkout feat/hardening-client-agent

```


3. **Read the Story & Requirements:** Every branch contains a detailed `CLIENT_REQUIREMENT.md` explaining the background chaos, what the client *thinks* they want, what you actually need to build, and the explicit "Definition of Done".
4. **Inspect & Run the Code:**
* Create a virtual environment: `python -m venv venv && source venv/bin/activate`
* Install dependencies: `pip install -r requirements.txt`
* Set up your `.env` configuration from `.env.example`.
* Run the application scripts and accompanying test suites (`python -m unittest discover src/`).



## 🎓 Masterclass Instructor

**Lead Instructor:** Ajay Meena

*Forward Deployed Engineering & System Architecture Masterclass*
