import requests

class VirusTotal:
    URL = "https://www.virustotal.com/api/v3/intelligence/search"

    def __init__(self, api_key):
        self.api_key = api_key

    def fetch(self):
        headers = {"x-apikey": self.api_key}
        params = {"query": "type:ip", "limit": 20}

        try:
            res = requests.get(self.URL, headers=headers, params=params, timeout=10).json()
        except Exception as e:
            print(f"Error fetching VirusTotal: {e}")
            return []

        data = []
        
        for item in res.get("data", []):
            attributes = item.get("attributes", {})
            data.append({
                "indicator": item.get("id"),
                "type": "ip",
                "source": "VirusTotal",
                "created": attributes.get("last_analysis_date")
            })
        
        return data

