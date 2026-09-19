# Project 1: Zero-to-One Lead Triage Automation

Lightweight, deterministic B2B lead triage automation service parsing incoming raw payload metadata and evaluating operational urgency.

## Setup & Execution Guide

1. **Create Virtual Environment**:
   ```bash
   python -m venv venv
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment**:
   Copy `src/.env.example` to `src/.env` or project root `.env`:
   ```bash
   cp src/.env.example .env
   ```

4. **Run Application**:
   ```bash
   python src/app.py
   ```

5. **Run Tests**:
   ```bash
   python -m unittest src/test_app.py
   ```
