import os

blocked = set()

def block_ip(ip):
    if ip in blocked:
        return

    print(f"[BLOCK] {ip}")
    os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
    blocked.add(ip)
