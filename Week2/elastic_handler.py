from elasticsearch import Elasticsearch


# Connect to Elasticsearch
def connect_elasticsearch():
    try:
        es = Elasticsearch("http://localhost:9200")

        # Test connection properly
        es.info()
        print("Connected to Elasticsearch")

        return es

    except Exception as e:
        print("Connection error:", e)
        return None


# Create index with mapping
def create_index(es, index_name="threat-intel"):

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
        # Check if index exists
        if not es.indices.exists(index=index_name):
            es.indices.create(index=index_name, body=mapping)
            print("Index created:", index_name)
        else:
            print("Index already exists:", index_name)

    except Exception as e:
        print("Error creating index:", e)


# Insert documents into Elasticsearch
def insert_documents(es, records, index_name="threat-intel"):

    for record in records:
        try:
            es.index(index=index_name, document=record)
        except Exception as e:
            print("Error inserting record:", e)

    print("Inserted", len(records), "documents")