# Setup MongoDB with sample data

from pymongo import MongoClient

def setup_mongodb():
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["threat_db"]
    collection = db["indicators"]
    
    # Sample threat indicators
    sample_data = [
        {
            "ip": "192.168.1.10",
            "source": "otx",
            "timestamp": "2024-01-15T10:30:45Z",
            "threat": "malware",
            "confidence": 95
        },
        {
            "ip": "8.8.8.8",
            "source": "internal",
            "timestamp": "2024-01-15T10:35:12Z",
            "threat": "benign",
            "confidence": 10
        },
        {
            "ip": "45.33.32.156",
            "source": "abuseipdb",
            "timestamp": "2024-01-15T10:40:22Z",
            "threat": "botnet",
            "confidence": 88
        },
        {
            "ip": "103.21.244.0",
            "source": "virustotal",
            "timestamp": "2024-01-15T10:45:55Z",
            "threat": "phishing",
            "confidence": 82
        },
        {
            "ip": "10.0.0.5",
            "source": "internal",
            "timestamp": "2024-01-15T11:00:00Z",
            "threat": "suspicious",
            "confidence": 65
        }
    ]
    
    # Clear existing data
    collection.delete_many({})
    
    # Insert sample data
    result = collection.insert_many(sample_data)
    
    print(f"Inserted {len(result.inserted_ids)} records into threat_db.indicators")
    print("\nSample data inserted:")
    for doc in sample_data:
        print(f"  - {doc['ip']} ({doc['threat']}) - Confidence: {doc['confidence']}%")

if __name__ == "__main__":
    setup_mongodb()
