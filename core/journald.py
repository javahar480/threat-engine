import subprocess
import json

def read_logs():
    result = subprocess.run(
        ["journalctl", "-o", "json", "-n", "50"],
        capture_output=True,
        text=True
    )

    logs = []
    for line in result.stdout.splitlines():
        try:
            logs.append(json.loads(line))
        except:
            continue

    return logs
