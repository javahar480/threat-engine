from collections import defaultdict
import time

events = defaultdict(list)

def add_event(ip, event):
    now = time.time()
    events[ip].append((event, now))
    events[ip] = events[ip][-20:]

def detect_attack_pattern(ip):
    types = [e[0] for e in events[ip]]

    if "beaconing" in types and "new_ip" in types:
        return "multi_stage_attack"

    return None
