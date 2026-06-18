from backend.collector import get_ssh_logs
from backend.parser import parse_log_line
from backend.database import SessionLocal
from backend.models import Event

db = SessionLocal()

processed = 0
inserted = 0
skipped = 0

logs = get_ssh_logs()

for line in logs:

    processed += 1

    parsed = parse_log_line(line)

    if not parsed:
        continue

    existing = db.query(Event).filter(
        Event.raw_log == line
    ).first()

    if existing:
        skipped += 1
        continue

    event = Event(
	timestamp=parsed["timestamp"],
        event_type=parsed["event"],
        source_ip=parsed["ip"],
        raw_log=line
    )

    db.add(event)
    inserted += 1

db.commit()
db.close()

print(f"Processed: {processed}")
print(f"Inserted: {inserted}")
print(f"Skipped: {skipped}")
