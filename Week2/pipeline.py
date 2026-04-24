from pymongo import MongoClient
from normalizer import normalize_data
from scorer import add_risk_score
from elastic_handler import connect_elasticsearch, create_index, insert_documents


def load_data_from_mongodb():
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["threat_db"]
    collection = db["indicators"]
    
    # Fetch all documents
    data = list(collection.find())
    print(f"Fetching data from MongoDB...")
    return data


def run_pipeline():
    print("\n=== THREAT INTELLIGENCE PIPELINE ===\n")
    
    # Step 1: Fetch data from MongoDB
    print("Step 1: Fetching data from MongoDB...")
    raw_data = load_data_from_mongodb()
    print(f"Found {len(raw_data)} records\n")
    
    # Step 2: Normalize data
    print("Step 2: Normalizing data...")
    normalized_data = normalize_data(raw_data)
    
    # Step 3: Apply scoring
    print("\nStep 3: Applying scoring...")
    scored_data = [add_risk_score(record) for record in normalized_data]
    for record in scored_data:
        print(f"  {record['ip']} - Risk: {record['risk']} (Confidence: {record['confidence']})")
    
    # Step 4: Connect to Elasticsearch
    print("\nStep 4: Connecting to Elasticsearch...")
    es = connect_elasticsearch()
    
    # Step 5: Create index
    print("Creating index...")
    create_index(es)
    
    # Step 6: Send to Elasticsearch
    print("Sending to Elasticsearch...")
    insert_documents(es, scored_data)
    
    print("\nPipeline completed")


if __name__ == "__main__":
    run_pipeline()
