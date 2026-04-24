from core.sniffer import start_sniffing
from db.database import init_db

if __name__ == "__main__":
    print("[*] Threat Engine Started")
    init_db()

    start_sniffing(interface="eno1")
