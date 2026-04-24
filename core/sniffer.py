from scapy.all import sniff
from core.analyzer import analyze_packet

def start_sniffing(interface=None):
    print("[*] Starting packet capture...")

    sniff(
        iface=interface,
        prn=analyze_packet,
        store=0,
        filter="ip and not multicast"
    )
