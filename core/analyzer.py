from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.dns import DNS
from core.detector import detect_event
from core.process_map import get_process_info_by_ip_port
from core.behavior import track_connection
from utils.baseline import update_baseline
from utils.logger import log_event


def analyze_packet(packet):
    data = {}

    # 🌐 IP layer
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # 🚫 DROP multicast + broadcast noise
        if dst_ip.startswith("224.") or dst_ip.startswith("239."):
            return
        if dst_ip == "255.255.255.255":
            return

        data["src_ip"] = src_ip
        data["dst_ip"] = dst_ip

    # 🔌 Ports
    if packet.haslayer(TCP) or packet.haslayer(UDP):
        try:
            data["dst_port"] = packet.dport
        except:
            pass

    # 🌍 DNS parsing
    if packet.haslayer(DNS) and packet[DNS].qd:
        try:
            data["domain"] = packet[DNS].qd.qname.decode().strip(".")
        except:
            data["domain"] = "unknown"

    # 🧠 Behavior tracking
    if "dst_ip" in data:
        track_connection(data["dst_ip"])

    # 📊 Baseline learning
    update_baseline(data)

    # 🧬 Process mapping
    if "dst_ip" in data and "dst_port" in data:
        proc = get_process_info_by_ip_port(
            data["dst_ip"], data["dst_port"]
        )
        if proc:
            data["process"] = proc

    # 📢 Output + detection
    if data:
        print(data)  # live debug
        log_event(data)
        detect_event(data)
