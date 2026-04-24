import json
from datetime import datetime

def log_event(data):
    with open("logs/events.json", "a") as f:
        f.write(json.dumps({"timestamp": str(datetime.now()), "data": data}) + "\n")

def log_alert(alert):
    print("[ALERT]", alert)
    with open("logs/alerts.json", "a") as f:
        f.write(json.dumps(alert) + "\n")
