import sys
import os

sys.path.append(os.path.abspath("."))

from backend.parser import parse_log_line
from backend.detector import detect_brute_force

events = []

with open("logs/sample.log") as file:
    for line in file:
        parsed = parse_log_line(line)

        if parsed:
            events.append(parsed)

alerts = detect_brute_force(events)

print(alerts)
