from backend.database import SessionLocal
from backend.models import Event

db = SessionLocal()

events = db.query(Event).all()

for event in events:
    print(
        event.id,
	event.timestamp,
        event.event_type,
        event.source_ip
    )

db.close()
