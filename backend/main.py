from fastapi import FastAPI
from backend.detector import detect_brute_force
from backend.database import SessionLocal
from backend.models import Event,Alert
from backend.ingestor import ingest_ssh_logs
from backend.alert_engine import generate_alerts


app = FastAPI(
    title="ThreatHawk",
    version="1.0.0"
)



@app.get("/")
def root():
    return {
        "message": "ThreatHawk API Running"
    }

@app.get("/events")
def get_events():

    db = SessionLocal()

    events = db.query(Event).all()

    results = []

    for event in events:
        results.append(
            {
                "id": event.id,
		"timestamp":event.timestamp,
                "event_type": event.event_type,
                "source_ip": event.source_ip
            }
        )

    db.close()

    return results

@app.get("/stats")
def get_stats():

    db = SessionLocal()

    total_events = db.query(Event).count()

    failed_logins = db.query(Event).filter(
        Event.event_type == "failed_login"
    ).count()

    successful_logins = db.query(Event).filter(
        Event.event_type == "successful_login"
    ).count()

    db.close()

    return {
        "total_events": total_events,
        "failed_logins": failed_logins,
        "successful_logins": successful_logins
    }

@app.get("/alerts")
def get_alerts():

    db = SessionLocal()

    alerts = db.query(Alert).all()

    results = []

    for alert in alerts:

        results.append(
            {
                "id": alert.id,
                "timestamp": alert.timestamp,
                "alert_type": alert.alert_type,
                "severity": alert.severity,
                "source_ip": alert.source_ip,
                "description": alert.description
            }
        )

    db.close()

    return results


@app.post("/ingest")
def ingest():

    ingest_stats = ingest_ssh_logs()

    alert_stats = generate_alerts()

    return {
        **ingest_stats,
        **alert_stats
    }
