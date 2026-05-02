import os

SAFE_MODE = True


def block_ip(ip):
    if SAFE_MODE:
        print(f"Simulated block for IP: {ip}")
    else:
        os.system(f"iptables -A INPUT -s {ip} -j DROP")
    
    print(f"Blocked IP: {ip}")
