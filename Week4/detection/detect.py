# detect.py

import re
from datetime import datetime


def detect_threat(log_data):
    """
    Detects common cyber attack patterns.
    """

    threat_patterns = {
        "SQL Injection": [
            r"(\%27)|(\')|(\-\-)|(\%23)|(#)",
            r"(?i)(union select)",
            r"(?i)(or 1=1)",
        ],

        "XSS Attack": [
            r"<script.*?>.*?</script>",
            r"javascript:",
            r"alert\s*\(",
        ],

        "Directory Traversal": [
            r"\.\./",
            r"\.\.\\",
        ],

        "Command Injection": [
            r";\s*ls",
            r";\s*cat",
            r"\|\s*whoami",
        ],

        "Brute Force": [
            r"failed login",
            r"invalid password",
            r"authentication failed",
        ]
    }

    detected = []

    for threat, patterns in threat_patterns.items():

        for pattern in patterns:

            if re.search(pattern, log_data, re.IGNORECASE):
                detected.append(threat)
                break

    result = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "log": log_data,
        "threat_detected": len(detected) > 0,
        "threats": detected
    }

    return result
