from core.scorer import calculate_score
from utils.logger import log_alert
from core.behavior import is_beaconing
from utils.baseline import is_new_ip
# from response.firewall import block_ip   # 🚫 KEEP DISABLED
from core.correlator import add_event, detect_attack_pattern
from intel.mitre import map_to_mitre
from db.database import insert_alert
from datetime import datetime


def detect_event(data):
    flags = {}
    ip = data.get("dst_ip")

    # 🚫 Ignore local/internal traffic
    if ip and (ip.startswith("192.168.") or ip.startswith("10.") or ip.startswith("172.")):
        return

    # 🆕 New IP detection (only external)
    if ip and is_new_ip(ip):
        flags["new_ip"] = True

    # 📡 Beaconing detection
    if ip and is_beaconing(ip):
        flags["beaconing"] = True

    # 🧠 Process validation (smarter whitelist)
    if "process" in data:
        pname = data["process"].get("process_name", "").lower()

        trusted = [
            "firefox",
            "chrome",
            "brave",
            "curl",
            "systemd",
            "systemd-resolved",
            "networkmanager",
            "dhclient"
        ]

        if pname and pname not in trusted:
            flags["unknown_process"] = True

    # 🚫 If no flags → ignore (reduces noise)
    if not flags:
        return

    # 🎯 Score calculation
    score = calculate_score(data, flags)

    # 🚨 Alert threshold
    if score >= 50:
        for f in flags:
            add_event(ip, f)

        pattern = detect_attack_pattern(ip)
        threat = pattern if pattern else ",".join(flags.keys())
        mitre = map_to_mitre(threat)

        alert = {
            "ip": ip,
            "flags": flags,
            "score": score,
            "mitre": mitre
        }

        log_alert(alert)

        insert_alert(
            str(datetime.now()),
            ip,
            f"{threat} ({mitre})",
            score
        )

        # 🚫 DO NOT ENABLE THIS YET
        # if score >= 80 and ip:
        #     block_ip(ip)
