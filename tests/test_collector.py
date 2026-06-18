from backend.collector import get_ssh_logs

logs = get_ssh_logs()

for line in logs:
    print(line)
