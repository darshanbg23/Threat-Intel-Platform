import requests

class AbuseCH:
    URL = "https://feodotracker.abuse.ch/downloads/ipblocklist.json"

    def fetch(self):
        try:
            res = requests.get(self.URL, timeout=10).json()
        except Exception as e:
            print(f"Error fetching AbuseCH: {e}")
            return []

        data = []
        
        for item in res:
            data.append({
                "indicator": item.get("ip_address"),
                "type": "ip",
                "source": "AbuseCH",
                "created": item.get("first_seen")
            })
        
        return data

