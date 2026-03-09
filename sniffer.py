from scapy.all import sniff, IP, DNS, DNSQR, conf
from datetime import datetime

# IMPORTANT: Setting your Wi-Fi interface (Intel Wi-Fi 6)
# Based on your screenshot, Index 14 is the correct one.
conf.iface = "Intel(R) Wi-Fi 6 AX201 160MHz" 

def process_packet(packet):
    try:
        timestamp = datetime.now().strftime('%H:%M:%S')
        
        # Capture Website Names (DNS)
        if packet.haslayer(DNS) and packet.haslayer(DNSQR):
            if packet.getlayer(DNS).qr == 0:
                query_name = packet.getlayer(DNSQR).qname.decode('utf-8', errors='ignore')
                print(f"[{timestamp}] [!] WEBSITE: {query_name}")
        
        # Capture General IP Traffic
        elif packet.haslayer(IP):
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            print(f"[{timestamp}] [+] TRAFFIC: {src_ip:15} ---> {dst_ip}")

    except Exception:
        pass

print("="*65)
print("   STABLE NETWORK ANALYZER v2.3 - FIXED INTERFACE MODE")
print(f"   Interface: {conf.iface}")
print("   Press Ctrl+C to Stop Monitoring")
print("="*65)

try:
    sniff(iface=conf.iface, prn=process_packet, store=False)
except PermissionError:
    print("\n[!] ERROR: Please run VS Code as Administrator.")
except KeyboardInterrupt:
    print("\n[#] Session Terminated.")