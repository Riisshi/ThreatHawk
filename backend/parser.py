import re
from datetime import datetime

CURRENT_YEAR = datetime.now().year


def extract_timestamp(line):
    try:
        timestamp_str = " ".join(line.split()[:3])

        dt = datetime.strptime(
            f"{CURRENT_YEAR} {timestamp_str}",
            "%Y %b %d %H:%M:%S"
        )

        return dt

    except Exception:
        return None


def parse_log_line(line):

    timestamp = extract_timestamp(line)

    failed_match = re.search(
        r"Failed password for .* from ([^\s]+)",
        line
    )

    if failed_match:
        return {
            "timestamp": timestamp,
            "event": "failed_login",
            "ip": failed_match.group(1)
        }

    success_match = re.search(
        r"Accepted password for .* from ([^\s]+)",
        line
    )

    if success_match:
        return {
            "timestamp": timestamp,
            "event": "successful_login",
            "ip": success_match.group(1)
        }

    return None
