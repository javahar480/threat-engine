from collections import defaultdict
import time

tracker = defaultdict(list)

def track_connection(ip):
    now = time.time()
    tracker[ip].append(now)

    # keep last 15 timestamps (more data = better accuracy)
    tracker[ip] = tracker[ip][-15:]


def is_beaconing(ip):
    t = tracker[ip]

    # need enough samples
    if len(t) < 6:
        return False

    # calculate intervals
    intervals = [t[i] - t[i-1] for i in range(1, len(t))]

    avg = sum(intervals) / len(intervals)

    # 🚫 ignore fast traffic (browser, CDN, etc.)
    if avg < 5:
        return False

    # 🎯 check consistency (low variance)
    stable = all(abs(i - avg) < 1.5 for i in intervals)

    # 🎯 check minimum duration (avoid short bursts)
    duration = t[-1] - t[0]

    if stable and duration > 20:
        return True

    return False
