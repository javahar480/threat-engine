# 🛡 Threat Engine (Mini EDR/NDR)

A lightweight, Linux-based **Threat Detection Engine** built from scratch using Python.
This project monitors network traffic in real time, correlates processes, and detects suspicious behavior using custom logic.

---

## 🚀 Features

* 📡 **Real-Time Packet Capture** (Scapy)
* 🧠 **Behavioral Analysis (Beaconing Detection)**
* 🔍 **Process-Level Correlation**
* 🎯 **Alert Scoring System**
* 🧬 **MITRE ATT&CK Mapping**
* 📝 **Structured Logging & Alerts**
* ⚡ **Lightweight CLI-Based Monitoring**

---

## 🧠 How It Works

1. Captures network packets from system interfaces
2. Extracts IP, port, and domain information
3. Maps traffic to running processes
4. Tracks connection behavior over time
5. Detects anomalies like:

   * Beaconing activity
   * Unknown processes
   * New external IPs
6. Assigns a risk score and generates alerts

---

## 🛠 Tech Stack

* **Python**
* **Scapy**
* **Psutil**
* **Requests**
* Linux Networking Tools

---

## ⚙️ Installation

```bash
sudo pacman -S python python-pip tcpdump net-tools
pip install scapy psutil requests
```

---

## ▶️ Usage

```bash
sudo python3 main.py
```

---

## 🧪 Example Output

```bash
[*] Threat Engine Started
[*] Starting packet capture...

{'src_ip': '192.168.1.x', 'dst_ip': '104.x.x.x', 'dst_port': 443, 'process': {'pid': 6366, 'process_name': 'brave'}}

[ALERT] {'ip': '104.x.x.x', 'flags': {'beaconing': True}, 'score': 80, 'mitre': 'T1071'}
```

---

## ⚠️ Disclaimer

This tool is intended for **educational and authorized security testing only**.
Do not use it on networks you do not own or have permission to monitor.

---

## 📌 Future Improvements

* 🌐 Threat Intelligence Integration (VirusTotal)
* 📊 Baseline Learning System
* 🖥 CLI Dashboard / Web UI
* 🔒 Safe Auto-Response System

---

## 👨‍💻 Author

**Javahar**
GitHub: https://github.com/javahar480

---

## ⭐ If you like this project

Give it a star ⭐ and feel free to contribute!
