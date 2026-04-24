from pymongo import MongoClient

class ThreatDB:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="threat_db"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["indicators"]
    
    
    # Check if IP already exists
    def ip_exists(self, ip):
        result = self.collection.find_one({"ip": ip})
        return result is not None
    
    
    # Insert records with duplicate check
    def insert(self, data):
        if not data:
            print("No data to insert")
            return
        
        inserted = 0
        duplicates = 0
        
        for item in data:
            ip = item.get("ip")
            
            if self.ip_exists(ip):
                duplicates += 1
                continue
            
            self.collection.insert_one(item)
            inserted += 1
        
        print(f"Database: Inserted {inserted} | Duplicates {duplicates}")
    
    
    # Get all records
    def get_all(self):
        return list(self.collection.find({}, {"_id": 0}))
    
    
    # Count total records
    def count(self):
        return self.collection.count_documents({})
    
    
    # Close connection
    def close(self):
        self.client.close()


