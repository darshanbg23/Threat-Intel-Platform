import subprocess
from pymongo import MongoClient

SAFE_MODE = True


def unblock_ip(ip):
    print(f"Unblocking IP: {ip}")

    if SAFE_MODE:
        print(f"Simulated unblock for IP: {ip}")
    else:
        subprocess.run(["sudo", "iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"])

    print("IP unblocked successfully")

    client = MongoClient("mongodb://localhost:27017/")
    db = client["threat_db"]
    collection = db["indicators"]

    collection.update_one(
        {"ip": ip},
        {"$set": {"blocked": False, "action": "unblocked"}}
    )

    print(f"Database updated for IP: {ip}")

    client.close()


if __name__ == "__main__":
    ip = "185.220.101.25"
    unblock_ip(ip)