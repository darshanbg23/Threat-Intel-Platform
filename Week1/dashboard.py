from flask import Flask, render_template
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)


# Get data from MongoDB
def get_threat_data():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["threat_db"]
        collection = db["indicators"]
        
        data = list(collection.find({}, {"_id": 0}))
        client.close()
        
        return data
    except Exception as e:
        print(f"Database error: {e}")
        return []


# Calculate statistics
def get_stats(data):
    if not data:
        return {
            "total": 0,
            "sources": 0,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    sources = set()
    for item in data:
        sources.add(item.get("source", "unknown"))
    
    stats = {
        "total": len(data),
        "sources": len(sources),
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    return stats


@app.route("/")
def index():
    data = get_threat_data()
    stats = get_stats(data)
    
    # Add index to data for table display
    indexed_data = list(enumerate(data, 1))
    
    return render_template(
        "index.html",
        total=stats["total"],
        sources=stats["sources"],
        last_updated=stats["last_updated"],
        data=indexed_data
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)

