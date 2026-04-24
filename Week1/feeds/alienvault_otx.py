import requests

class AlienVaultOTX:
    URL = "https://otx.alienvault.com/api/v1/pulses/subscribed"

    def __init__(self, api_key):
        self.api_key = api_key

    def fetch(self):
        headers = {"X-OTX-API-KEY": self.api_key}
        
        try:
            res = requests.get(self.URL, headers=headers, timeout=10).json()
        except Exception as e:
            print(f"Error fetching OTX: {e}")
            return []

        data = []
        
        for pulse in res.get("results", []):
            for indicator in pulse.get("indicators", []):
                data.append({
                    "indicator": indicator.get("indicator"),
                    "type": indicator.get("type"),
                    "source": "AlienVault OTX",
                    "created": pulse.get("created")
                })
        
        return data

