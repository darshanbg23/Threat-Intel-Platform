import os
from datetime import datetime

BLOCKED_IPS_FILE = "blocked_ips.txt"
LOG_FILE = "logs/firewall.log"

os.makedirs("logs", exist_ok=True)

def block_ip(ip):
    with open(BLOCKED_IPS_FILE, "a") as file:
        file.write(ip + "\n")

    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - BLOCKED IP: {ip}\n")

    print(f"[+] IP Blocked: {ip}")

suspicious_ip = input("Enter suspicious IP: ")

block_ip(suspicious_ip)
