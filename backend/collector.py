import subprocess

def get_ssh_logs(lines=50):

    result = subprocess.run(
        ["journalctl", "-u", "ssh", "-n", str(lines)],
        capture_output=True,
        text=True
    )

    return result.stdout.splitlines()
