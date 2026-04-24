baseline_ips = set()

def update_baseline(data):
    if "dst_ip" in data:
        baseline_ips.add(data["dst_ip"])

def is_new_ip(ip):
    return ip not in baseline_ips
