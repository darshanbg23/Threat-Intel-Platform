#policy engine 
import time
from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME, SLEEP_TIME
from firewall import block_ip
blocked_ips = set()
def connect_db():
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
cat /home/kali/.ssh/id_ed25519.pubcollection = db[COLLECTION_NAME]
return collection
def get_high_risk_ips():
print("Checking MongoDB...")
collection = connect_db()
records = list(collection.find())
ips = []
for record in records:
ip = record.get("ip")
risk = record.get("risk", "LOW")
confidence = record.get("confidence", 0)
if ip is None:
continue
if risk == "HIGH" or confidence >= 70:
ips.append(ip)
print(f"Found {len(ips)} high-risk IPs")
return ips
4
def run_policy_engine():
print("Starting Policy Engine")
while True:
ips = get_high_risk_ips()
for ip in ips:
if ip not in blocked_ips:
print(f"Blocking IP: {ip}")
block_ip(ip)
blocked_ips.add(ip)
else:
print(f"Already blocked: {ip}")
time.sleep(SLEEP_TIME)
if __name__ == "__main__":
run_policy_engine()
