# Network-Traffic-Analyzer
A high-performance Python-based network security tool designed for real-time packet interception, protocol analysis, and DNS monitoring. Built with Scapy for deep packet inspection.
# 🛡️ NetSentinel-Py: Real-Time Network Traffic Analyzer

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Security](https://img.shields.io/badge/Security-Data-red?style=for-the-badge)

A professional-grade networking tool built with **Python** and **Scapy** to monitor, intercept, and analyze live network packets. This project is designed for security auditing and understanding the flow of data within a local network.

### 🚀 Key Features
* **Live Packet Interception:** Captures real-time IP, TCP, and UDP traffic on the local interface.
* **DNS Intelligence:** Identifies domain requests (e.g., WhatsApp, Wikipedia) to monitor background app activity.
* **Hardware-Specific Monitoring:** Configured for high-performance interfaces like Intel(R) Wi-Fi 6 AX201.
* **Time-Stamped Logging:** Every captured packet includes a precise system timestamp for forensic analysis.
* **Robust Error Handling:** Built-in protection against malformed packets and permission errors.
* **SQL Injection Scanner:** An advanced tool to detect database vulnerabilities using multiple heuristic payloads.

### 🛠️ Technical Stack
* **Language:** Python 3.13
* **Core Library:** Scapy (Packet Manipulation)
* **Driver:** Npcap (Packet Capture Driver for Windows)
* **IDE:** VS Code (Administrator Mode)

### 📊 How It Works
The script uses a low-level socket to listen to the specified network interface (Index 14). It filters incoming data into readable formats, displaying source/destination IPs and visited website domains instantly.
