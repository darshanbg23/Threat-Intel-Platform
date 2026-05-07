import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ====================================================
# CONFIGURATION
# ====================================================

PFSENSE_HOST = "https://YOUR_PFSENSE_IP"
API_KEY = "YOUR_API_KEY"

# ====================================================
# BLOCK FUNCTION
# ====================================================

def block_ip(ip):

    url = f"{PFSENSE_HOST}/api/v1/firewall/rule"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "type": "block",
        "interface": "wan",
        "ipprotocol": "inet",
        "source": {
            "address": ip
        },
        "descr": "Blocked by SOAR"
    }

    try:

        print(f"[*] Connecting to pfSense: {PFSENSE_HOST}")

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            verify=False,
            timeout=30
        )

        print(f"[*] Status Code: {response.status_code}")

        if response.status_code in [200, 201]:

            print(f"[+] Successfully blocked IP: {ip}")

        else:

            print("[-] API Error")
            print(response.text)

    except requests.exceptions.ConnectTimeout:

        print("[-] Connection Timeout")
        print("[!] pfSense is unreachable")

    except requests.exceptions.ConnectionError:

        print("[-] Connection Error")
        print("[!] Check pfSense IP Address")

    except Exception as e:

        print(f"[-] Unknown Error: {e}")

# ====================================================
# TEST
# ====================================================

if __name__ == "__main__":

    block_ip("192.168.1.50")
