# Project 2 (V1): Vulnerable Client Agent Prototype

This prototype demonstrates common security vulnerabilities in unhardened client AI agents.

## Known Vulnerabilities in V1

1. **Unredacted PII Exposure**: User inputs containing Social Security Numbers (SSN), phone numbers, or email addresses are passed directly to downstream model APIs without redaction or scrubbing.
2. **Prompt Injection Susceptibility**: System prompts and instruction guardrails can be bypassed via prompt injection keywords (e.g. `System Override`), leading to key leakage or unauthorized instructions.

## Verification

Run the vulnerability demonstration script:
```bash
py -3.12 src/test_vulnerabilities.py
```
Both PII leakage and prompt injection exploitation will be demonstrated in console output.
