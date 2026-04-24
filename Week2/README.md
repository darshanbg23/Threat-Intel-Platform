# Threat Intelligence Processing & SIEM - Week 2

## Overview

Week 2 processes the threat data collected in Week 1 and prepares it for security analysis. This module normalizes data structures, applies risk scoring based on confidence levels, and integrates with Elasticsearch and Kibana for visualization and monitoring.

Week 2 reads threat indicators from the MongoDB database populated by Week 1 and enriches them with risk metrics.

---

## What This Module Does

- Normalizes threat data from MongoDB to ensure consistent structure
- Applies risk scoring based on confidence values
- Integrates with Elasticsearch for indexing and search
- Provides visualization capabilities through Kibana
- Uses Docker for containerized deployment of the ELK stack

---

## Objectives

✅ Normalize threat data structure  
✅ Add risk scoring to each indicator  
✅ Send data to Elasticsearch  
✅ Visualize data in Kibana  

---

## Key Components

```
Week2/
├── pipeline.py          ← Main pipeline that runs everything
├── normalizer.py        ← Formats data to be consistent
├── scorer.py            ← Adds risk level and confidence
├── elastic_handler.py   ← Connects to Elasticsearch
├── setup_mongodb.py     ← Creates sample data
├── docker-compose.yml   ← Runs MongoDB, Elasticsearch, Kibana
└── data/                ← Sample data files
```

### What Each File Does

| File | Purpose |
|------|---------|
| `pipeline.py` | Runs the entire pipeline from start to finish |
| `normalizer.py` | Makes sure all data has the same format (ip, source, timestamp) |
| `scorer.py` | Looks at confidence and assigns a risk level |
| `elastic_handler.py` | Sends data to Elasticsearch and creates the index |
| `docker-compose.yml` | Starts MongoDB, Elasticsearch, and Kibana in Docker |

---

## Data Flow

```
MongoDB (Week 1 data)
    ↓
Normalize (consistent format)
    ↓
Score (add risk levels)
    ↓
Elasticsearch (store for searching)
    ↓
Kibana (visualize on dashboard)
```

---

## How It Works

### Step 1: Fetch
- Pull all threat data from MongoDB (what Week 1 collected)

### Step 2: Normalize
- Make sure every entry has: IP, source, timestamp
- Remove incomplete entries

### Step 3: Score
- Evaluate confidence level (0-100)
- Assign risk level:
  - HIGH: confidence > 80
  - MEDIUM: 50 < confidence ≤ 80
  - LOW: confidence ≤ 50
### Step 4: Send to Elasticsearch
- Create an index called `threat-intel`
- Insert all scored threats

### Step 5: Visualize in Kibana
- Open Kibana dashboard
- Create visualizations
- Monitor threats

---

## Setup Instructions

### Step 1: Install Dependencies

```bash
pip install pymongo elasticsearch
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

### Step 2: Start the ELK Stack

```bash
docker-compose up -d
```

This starts:
- **MongoDB** on port 27017
- **Elasticsearch** on port 9200
- **Kibana** on port 5601

Wait a few seconds for services to start.

### Step 3: Verify Services Are Running

```bash
docker ps
```

You should see 3 containers running.

---

## Run the Pipeline

### Step 1: Populate MongoDB (Optional)

If you want to test with sample data:
```bash
python setup_mongodb.py
```

This creates some test threats in MongoDB.

### Step 2: Run the Pipeline

```bash
python pipeline.py
```

You'll see output like:
```
=== THREAT INTELLIGENCE PIPELINE ===

Step 1: Fetching data from MongoDB...
Found 10 records

Step 2: Normalizing data...
Normalized 10 records

Step 3: Applying scoring...
  192.168.1.10 - Risk: HIGH (Confidence: 95)
  8.8.8.8 - Risk: LOW (Confidence: 10)

Step 4: Connecting to Elasticsearch...
Connected to Elasticsearch

Creating index...
Created index: threat-intel

Sending to Elasticsearch...
Inserted 10 documents

Pipeline completed
```

---

## Using Kibana

### Open Kibana

Go to: **http://localhost:5601**

### Create Index Pattern

1. Click **Stack Management** (left sidebar)
2. Click **Index Patterns**
3. Click **Create Index Pattern**
4. Enter: `threat-intel`
5. Click **Create**

### View Your Data

1. Click **Discover** (left sidebar)
2. Select `threat-intel` index
3. You'll see all your threat data!

### Create Visualizations

1. Click **Visualize** (left sidebar)
2. Click **Create Visualization**
3. Choose visualization type (Bar chart, Table, etc.)
4. Select your data
## Risk Scoring Methodology

Each threat indicator is scored based on confidence values:

| Risk Level | Confidence Range | Interpretation |
|-----------|------------------|----------------|
| HIGH | confidence > 80 | Highly likely to be malicious |
| MEDIUM | 50 < confidence ≤ 80 | Likely to be malicious |
| LOW | confidence ≤ 50 | Possibly malicious or unknown |

---

## What Gets Sent to Elasticsearch

Each threat has:
- **ip** → The threat IP address
- **source** → Where it came from (OTX, VirusTotal, etc.)
- **timestamp** → When it was collected
- **risk** → Threat level (HIGH, MEDIUM, LOW)
- **confidence** → Confidence percentage

---

## Troubleshooting

**Elasticsearch not connecting?**
```bash
docker ps
```
If container is not running, restart:
```bash
docker-compose restart elasticsearch
```

**MongoDB connection error?**
- Make sure Week 1 ran successfully
- Check MongoDB is running: `docker ps`

**Kibana not loading?**
- Wait 30 seconds for services to fully start
- Refresh the page
- Check: http://localhost:5601

**No data in Elasticsearch?**
- Run `python setup_mongodb.py` to create sample data
- Run `python pipeline.py` again

---

## Notes

- **Week 2 Dependency** - Week 2 requires data populated in MongoDB by Week 1
- **Docker Required** - Docker and Docker Compose must be installed to run Elasticsearch and Kibana
- **Local Deployment** - This setup runs on localhost (127.0.0.1) for development purposes
- **Test Data** - Use `setup_mongodb.py` to populate sample threat indicators for testing
- **Index Naming** - The Elasticsearch index is named `threat-intel` for all threat data

---

## Next Steps After Week 2

- Explore Kibana visualizations
- Create custom dashboards
- Try filtering and searching data
- Understand risk scoring in action

---

