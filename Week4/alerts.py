import json
from datetime import datetime

ALERT_FILE = "logs/alerts.json"

def send_alert(ip, reason):
    alert = {
        "timestamp": str(datetime.now()),
        "ip": ip,
        "reason": reason,
        "status": "blocked"
    }

    with open(ALERT_FILE, "a") as file:
        json.dump(alert, file)
        file.write("\n")

    print("[+] Alert Logged")
