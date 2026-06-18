from datetime import datetime, UTC

from backend.database import SessionLocal
from backend.models import Event, Alert
from backend.detector import detect_brute_force


def generate_alerts():

    db = SessionLocal()

    events = []

    records = db.query(Event).all()

    for record in records:
        events.append(
            {
                "event": record.event_type,
                "ip": record.source_ip,
                "timestamp": record.timestamp
            }
        )

    alerts = detect_brute_force(events)

    created = 0

    for alert in alerts:

        existing = db.query(Alert).filter(
            Alert.alert_type == alert["alert_type"],
            Alert.source_ip == alert["ip"]
        ).first()

        if existing:
            continue

        new_alert = Alert(
            timestamp=datetime.now(UTC),
            alert_type=alert["alert_type"],
            severity=alert["severity"],
            source_ip=alert["ip"],
            description=f"Detected brute force activity from {alert['ip']}"
        )

        db.add(new_alert)
        created += 1

    db.commit()
    db.close()

    return {
        "alerts_created": created
    }