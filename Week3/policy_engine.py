import time
from pymongo import MongoClient
from config import (
    MONGO_URI,
    DB_NAME,
    COLLECTION_NAME,
    SLEEP_TIME,
    MAX_RUNS,
    RISK_THRESHOLD,
    CONFIDENCE_THRESHOLD
)
from firewall import block_ip

blocked_ips = set()


def connect_db():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db[COLLECTION_NAME]


def get_high_risk_ips(collection):
    print("Checking MongoDB...")

    records = list(collection.find())
    ips = []

    for record in records:
        ip = record.get("ip")
        risk = record.get("risk", "LOW")
        confidence = record.get("confidence", 0)

        if not ip:
            continue

        if risk == RISK_THRESHOLD or confidence >= CONFIDENCE_THRESHOLD:
            ips.append(ip)

    print(f"Found {len(ips)} high-risk IPs")

    return ips


def run_policy_engine():
    print("Starting Policy Engine")

    collection = connect_db()

    for _ in range(MAX_RUNS):
        ips = get_high_risk_ips(collection)

        if not ips:
            print("No high-risk IPs found")

        for ip in ips:
            if ip not in blocked_ips:
                print(f"Blocking IP: {ip}")
                block_ip(ip)
                blocked_ips.add(ip)
            else:
                print(f"Already blocked: {ip}")

        time.sleep(SLEEP_TIME)

    print("Policy Engine Finished")


if __name__ == "__main__":
    run_policy_engine()