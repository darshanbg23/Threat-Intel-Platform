from elasticsearch import Elasticsearch

def connect_elasticsearch():
    try:
        es = Elasticsearch(
            "http://localhost:9200",
            verify_certs=False,
            request_timeout=30
        )

        if es.ping():
            print("Connected to Elasticsearch")
            return es
        else:
            raise Exception("Elasticsearch not reachable")

    except Exception as e:
        print("Connection error:", e)
        raise


def create_index(es, index_name="threat-intel"):
    # Create index with field mapping
    mapping = {
        "mappings": {
            "properties": {
                "ip": {"type": "ip"},
                "source": {"type": "keyword"},
                "timestamp": {"type": "date"},
                "threat": {"type": "keyword"},
                "risk": {"type": "keyword"},
                "confidence": {"type": "integer"}
            }
        }
    }
    
    try:
        if not es.indices.exists(index=index_name):
            es.indices.create(index=index_name, body=mapping)
            print(f"Created index: {index_name}")
        else:
            print(f"Index already exists: {index_name}")
    except Exception as e:
        print(f"Error creating index: {e}")


def insert_documents(es, records, index_name="threat-intel"):
    # Insert records into Elasticsearch
    for i, record in enumerate(records):
        try:
            es.index(index=index_name, id=i, body=record)
        except Exception as e:
            print(f"Error inserting record {i}: {e}")
    
    print(f"Inserted {len(records)} documents")

