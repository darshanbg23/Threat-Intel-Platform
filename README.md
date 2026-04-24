# Threat Intelligence Platform

A beginner-friendly cybersecurity internship project that collects, processes, and visualizes threat intelligence data.

---

## Project Overview

This project demonstrates how to build a threat intelligence pipeline for learning purposes. It consists of two modules:

1. **Week 1** - Collects threat data from multiple OSINT sources and stores it in MongoDB
2. **Week 2** - Processes the data, applies risk scoring, and integrates with Elasticsearch and Kibana

This implementation demonstrates a simplified SIEM (Security Information and Event Management) pipeline suitable for educational purposes.

---

## Project Flow

```
OSINT Sources
    ↓
Fetch Data (Week 1)
    ↓
Clean & Store in MongoDB (Week 1)
    ↓
Normalize Data (Week 2)
    ↓
Add Risk Scoring (Week 2)
    ↓
Send to Elasticsearch (Week 2)
    ↓
Visualize in Kibana (Week 2)
```

---

## Architecture

### Week 1 Pipeline
```
OSINT Sources → Fetch → Clean → MongoDB
```

### Week 2 Pipeline
```
MongoDB → Normalize → Score → Elasticsearch → Kibana
```

Week 2 uses threat data stored in MongoDB by Week 1 as its primary data source.

---

## What's Included

### Week 1: Data Collection & Storage

Focuses on gathering threat intelligence from public sources:

- Fetches from multiple OSINT sources (AlienVault OTX, VirusTotal, AbuseIPDB)
- Validates and cleans data (IP format verification, duplicate removal)
- Stores validated indicators in MongoDB
- Exports results to CSV and JSON formats

**Output:** Threat indicators stored in MongoDB; CSV and JSON exports in `reports/`

### Week 2: Processing & SIEM Integration

Enriches and visualizes threat data from Week 1:

- Normalizes threat indicator structure for consistency
- Applies risk scoring based on confidence metrics
- Integrates with Elasticsearch for indexing and search capabilities
- Provides interactive visualizations and dashboards in Kibana

**Output:** Indexed threat intelligence accessible through Kibana interface

---

## Folder Structure

```
Threat Intelligence Platform/
│
├── Week1/                      ← Data Collection & Storage
│   ├── main.py                 ← Run the pipeline
│   ├── cleaner.py              ← Clean and validate data
│   ├── database.py             ← MongoDB operations
│   ├── exporter.py             ← Export to CSV/JSON
│   ├── feeds/                  ← OSINT source connectors
│   │   ├── alienvault_otx.py
│   │   ├── virustotal.py
│   │   └── abusech.py
│   ├── reports/                ← Output files
│   ├── requirements.txt
│   └── README.md               ← Week 1 guide
│
├── Week2/                      ← Processing & SIEM Integration
│   ├── pipeline.py             ← Run the pipeline
│   ├── normalizer.py           ← Normalize data
│   ├── scorer.py               ← Add risk scoring
│   ├── elastic_handler.py      ← Elasticsearch integration
│   ├── docker-compose.yml      ← ELK stack
│   ├── setup_mongodb.py        ← Sample data
│   ├── requirements.txt
│   └── README.md               ← Week 2 guide
│
└── README.md                   ← This file
```

---

## Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python** | Main programming language |
| **MongoDB** | Data storage (NoSQL) |
| **Elasticsearch** | Search and indexing |
| **Kibana** | Data visualization and dashboards |
| **Docker** | Container orchestration |

---

## Quick Start

### Prerequisites

- Python 3.8+
- Docker and Docker Compose
- MongoDB (can run in Docker)

### Step 1: Run Week 1 (Data Collection)

```bash
cd Week1

# Setup
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Make sure MongoDB is running
# Then run the pipeline
python main.py
```

This will:
- Fetch data from OSINT sources
- Clean and validate it
- Store in MongoDB
- Export to CSV and JSON

### Step 2: Run Week 2 (Processing & Visualization)

```bash
cd ../Week2

# Setup
pip install -r requirements.txt

# Start Docker services (MongoDB, Elasticsearch, Kibana)
docker-compose up -d

# Wait 30 seconds for services to start
# Then run the pipeline
python pipeline.py
```

This will:
- Fetch data from MongoDB
- Normalize and score it
- Send to Elasticsearch
- Get ready for Kibana

### Step 3: View in Kibana

1. Open: **http://localhost:5601**
2. Go to **Stack Management** → **Index Patterns**
3. Create pattern for `threat-intel`
4. Go to **Discover** and explore your data
5. Create visualizations on a dashboard

---

## Learning Outcomes

This project teaches:

- Data pipeline architecture and design
- OSINT (Open Source Intelligence) collection methods
- Data validation and deduplication techniques
- NoSQL database operations (MongoDB)
- Risk scoring and threat classification
- SIEM fundamentals and integration patterns
- Elasticsearch indexing and query optimization
- Kibana dashboard creation and visualization
- Docker containerization and orchestration  

---

## Project Features

- Multi-source data ingestion from 3 OSINT feeds
- IP address validation (IPv4 and IPv6)
- Duplicate detection and removal
- Risk scoring (HIGH/MEDIUM/LOW categories)
- Automated end-to-end data pipeline
- Elasticsearch integration for scalable indexing
- Interactive Kibana dashboards for threat visualization
- Docker-based deployment for easy setup

---

## How It Works

### Data Collection (Week 1)

```python
1. Fetch from AlienVault OTX
2. Fetch from VirusTotal
3. Fetch from AbuseIPDB
4. Combine all data
5. Validate and clean
6. Remove duplicates
7. Store in MongoDB
8. Export to files
```

### Data Processing (Week 2)

```python
1. Load from MongoDB
2. Normalize format
3. Score by risk level
4. Connect to Elasticsearch
5. Create index
6. Insert documents
7. Access in Kibana
```

---

## Troubleshooting

**MongoDB not starting?**
- Make sure MongoDB is running: `docker ps`
- Check port 27017 is available

**Elasticsearch connection error?**
- Wait 30 seconds for services to start
- Restart: `docker-compose restart elasticsearch`

**No data in Kibana?**
- Make sure Week 1 ran successfully
- Run `python setup_mongodb.py` to create sample data
- Run `python pipeline.py` again

For more details, see individual README files in Week1/ and Week2/

---

## Project Characteristics

- **Beginner-Level Implementation** - Code prioritizes clarity and learning over production optimizations
- **Educational Focus** - Designed to demonstrate concepts and best practices
- **Comprehensive Documentation** - Detailed README files in each folder and at project root
- **Containerized Architecture** - Docker Compose for simplified service deployment
- **Minimal Dependencies** - Only essential libraries and tools required

---

## Next Steps

After completing the project, you can:

1. Add more OSINT sources (AbuseIPDB, Shodan, etc.)
2. Create custom Kibana dashboards
3. Add email alerts for HIGH-risk threats
4. Integrate with a real SIEM platform
5. Deploy to cloud (AWS, Azure, GCP)

---

## File Guide

| File | What It Does |
|------|-------------|
| `Week1/README.md` | Week 1 detailed guide |
| `Week2/README.md` | Week 2 detailed guide |
| `Week1/main.py` | Runs Week 1 pipeline |
| `Week2/pipeline.py` | Runs Week 2 pipeline |
| `docker-compose.yml` | Starts ELK stack |

---

## Support and Documentation

For detailed information:
- Week 1 setup and execution: See `Week1/README.md`
- Week 2 setup and execution: See `Week2/README.md`
- Project structure overview: See this README.md

Each module contains specific troubleshooting guidance and usage examples.
