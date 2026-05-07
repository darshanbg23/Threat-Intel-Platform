import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

PFSENSE_HOST = "https://YOUR_PFSENSE_IP"
API_KEY = "YOUR_API_KEY"

def rollback_ip(ip):

    url = f"{PFSENSE_HOST}/api/v1/firewall/rule/{ip}"

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    try:

        response = requests.delete(
            url,
            headers=headers,
            verify=False,
            timeout=30
        )

        if response.status_code in [200, 204]:

            print(f"[+] Rollback Successful: {ip}")

        else:

            print("[-] Rollback Failed")
            print(response.text)

    except Exception as e:

        print(f"[-] Error: {e}")

if __name__ == "__main__":

    rollback_ip("192.168.1.50")
