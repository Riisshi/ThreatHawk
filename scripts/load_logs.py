from backend.parser import parse_log_line
from backend.database import SessionLocal
from backend.models import Event

db = SessionLocal()

with open("logs/sample.log") as file:
    for line in file:
        parsed = parse_log_line(line)

        if parsed:
            event = Event(
                event_type=parsed["event"],
                source_ip=parsed["ip"]
            )

            db.add(event)

db.commit()
db.close()

print("Logs loaded successfully.")
