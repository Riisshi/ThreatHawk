# ThreatHawk
![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)
![Status](https://img.shields.io/badge/Status-Active-success)

ThreatHawk is a lightweight SIEM-inspired security monitoring platform built with Python, FastAPI, SQLite, and Linux system logs.

It collects SSH authentication events from Linux journals, stores them in a database, detects brute-force login activity, generates security alerts, and exposes data through REST APIs.

---

## Features

- SSH log collection from systemd journal
- Event parsing and normalization
- SQLite event storage
- Duplicate event prevention
- Brute-force attack detection
- Alert generation and persistence
- FastAPI REST API
- Interactive Swagger documentation

---

## Architecture

```text
SSH Logs (journalctl)
        ↓
Collector
        ↓
Parser
        ↓
SQLite Database
        ↓
Detection Engine
        ↓
Alert Engine
        ↓
FastAPI API
```

---

## Screenshots

### API Documentation

![Swagger Dashboard](screenshots/swagger-dashboard.png)

### Events API

![Events API](screenshots/events-api.png)

### Alerts API

![Alerts API](screenshots/alerts-api.png)

### Ingestion Results

![Ingestion Results](screenshots/ingest-api.png)

### Database Events

![Database Events](screenshots/database-events.png)

---

## Tech Stack

- Python 3
- FastAPI
- SQLite
- SQLAlchemy
- Uvicorn
- Linux (Kali)
- Journalctl

---

## API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | `/` | Health Check |
| GET | `/events` | View stored events |
| GET | `/stats` | Event statistics |
| GET | `/alerts` | View generated alerts |
| POST | `/ingest` | Collect and process SSH logs |

---

## Detection Logic

### Brute Force Login Detection

ThreatHawk currently detects brute-force attacks using the following rule:

```text
5 failed login attempts
from the same IP address
within 5 minutes
```

### Alert Example

```json
{
  "alert_type": "brute_force",
  "severity": "high",
  "source_ip": "::1"
}
```

---

## Example Event

```json
{
  "id": 1,
  "timestamp": "2026-06-18T11:39:10",
  "event_type": "failed_login",
  "source_ip": "::1"
}
```

---

## Installation

### Clone Repository

```bash
git clone <repo-url>

cd ThreatHawk
```

### Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running ThreatHawk

### Create Database

```bash
python create_db.py
```

### Start API Server

```bash
uvicorn backend.main:app --reload
```

### Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

## Sample API Responses

### GET /stats

```json
{
  "total_events": 9,
  "failed_logins": 9,
  "successful_logins": 0
}
```

### POST /ingest

```json
{
  "processed": 50,
  "inserted": 0,
  "skipped": 9,
  "alerts_created": 0
}
```

### GET /alerts

```json
[
  {
    "id": 1,
    "timestamp": "2026-06-18T06:14:18",
    "alert_type": "brute_force",
    "severity": "high",
    "source_ip": "::1",
    "description": "Detected brute force activity from ::1"
  }
]
```

---

## Project Structure

```text
ThreatHawk/
│
├── backend/
│   ├── alert_engine.py
│   ├── collector.py
│   ├── database.py
│   ├── detector.py
│   ├── ingestor.py
│   ├── main.py
│   ├── models.py
│   └── parser.py
│
├── logs/
│
├── tests/
│
├── create_db.py
├── generate_alerts.py
├── ingest_ssh.py
├── requirements.txt
└── README.md
```

---

## Future Improvements

- Real-time monitoring
- Alert suppression windows
- Docker deployment
- Web dashboard
- Multiple log sources
- Email notifications
- Telegram alerts
- Threat intelligence integration
- Geo-IP enrichment
- MITRE ATT&CK mapping

---

## Author

**RishiKhanth**

B.Tech Computer Science & Systems Engineering  
Christ (Deemed to be University)

---

## License

This project is intended for educational and research purposes.