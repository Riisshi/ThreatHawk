from backend.database import SessionLocal
from backend.models import Alert

db = SessionLocal()

alerts = db.query(Alert).all()

for alert in alerts:
    print(
        alert.id,
        alert.timestamp,
        alert.alert_type,
        alert.severity,
        alert.source_ip
    )

db.close()

