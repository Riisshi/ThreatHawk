from collections import defaultdict
from datetime import timedelta

FAILED_LOGIN_THRESHOLD = 5
WINDOW_MINUTES = 5


def detect_brute_force(events):

    alerts = []

    failed_by_ip = defaultdict(list)

    for event in events:

        if event["event"] == "failed_login":

            failed_by_ip[event["ip"]].append(
                event["timestamp"]
            )

    for ip, timestamps in failed_by_ip.items():

        timestamps.sort()

        for i in range(len(timestamps)):

            count = 1

            for j in range(i + 1, len(timestamps)):

                delta = timestamps[j] - timestamps[i]

                if delta <= timedelta(
                    minutes=WINDOW_MINUTES
                ):
                    count += 1
                else:
                    break

            if count >= FAILED_LOGIN_THRESHOLD:

                alerts.append(
                    {
                        "alert_type": "brute_force",
                        "severity": "high",
                        "ip": ip,
                        "failed_attempts": count
                    }
                )

                break

    return alerts
