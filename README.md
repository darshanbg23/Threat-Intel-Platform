# Threat Intelligence Platform

A beginner-friendly cybersecurity project that collects, processes, and enforces threat intelligence with automated response.

---

## Project Overview

This project demonstrates a complete threat intelligence pipeline with three phases:

- **Week 1**: Collects threat data from multiple OSINT sources and stores in MongoDB
- **Week 2**: Processes data, applies risk scoring, and sends to Elasticsearch for visualization
- **Week 3**: Monitors threats and automatically blocks high-risk IPs using firewall rules

This implementation shows the full lifecycle of threat intelligence from collection to enforcement.

---

## Project Architecture

### Week 1: OSINT Data Collection
- Fetches data from multiple OSINT feeds (AlienVault OTX, VirusTotal, AbuseCH)
- Cleans and deduplicates the data
- Stores indicators in MongoDB

### Week 2: Data Processing and SIEM Integration
- Reads threat data from MongoDB
- Normalizes data to consistent format
- Applies risk scoring (HIGH/MEDIUM/LOW based on confidence)
- Sends enriched data to Elasticsearch
- Visualizable in Kibana dashboard

### Week 3: Dynamic Policy Enforcement
- Monitors MongoDB for high-risk indicators
- Detects IPs with risk=HIGH or confidence>=70
- Blocks malicious IPs using Linux firewall (iptables)
- Includes SAFE_MODE for testing without real blocking

---

## Folder Structure

```
Threat-Intel/
├── Week1/                    ← OSINT Ingestion
│   ├── main.py               ← Entry point for data collection
│   ├── database.py           ← MongoDB operations
│   ├── cleaner.py            ← Data cleaning logic
│   ├── exporter.py           ← Export to CSV/JSON
│   ├── feeds/                ← OSINT source connectors
│   ├── requirements.txt       ← Dependencies
│   └── README.md             ← Week 1 documentation
│
├── Week2/                    ← Data Processing & SIEM
│   ├── pipeline.py           ← Main data pipeline
│   ├── normalizer.py         ← Data normalization
│   ├── scorer.py             ← Risk scoring logic
│   ├── elastic_handler.py    ← Elasticsearch integration
│   ├── docker-compose.yml    ← Elasticsearch/Kibana setup
│   ├── requirements.txt       ← Dependencies
│   └── README.md             ← Week 2 documentation
│
├── Week3/                    ← Dynamic Policy Enforcement
│   ├── policy_engine.py      ← Main policy engine
│   ├── firewall.py           ← IP blocking logic
│   ├── config.py             ← Configuration
│   ├── requirements.txt       ← Dependencies
│   └── README.md             ← Week 3 documentation
│
└── README.md                 ← This file
```

---

## Prerequisites

### System Requirements
- Linux/Kali system (for iptables support in Week 3)
- Python 3.6 or higher
- MongoDB running locally
- Docker and docker-compose (for Week 2 Elasticsearch)

### Installation Prerequisites
```bash
# Install MongoDB (Ubuntu/Debian)
sudo apt-get install -y mongodb

# Install Docker
sudo apt-get install -y docker.io docker-compose

# Verify installations
mongod --version
docker --version
docker-compose --version
```

---

## Quick Start

Before running any week, set up the virtual environment once in the main project directory:

```bash
# Navigate to project directory
cd Threat-Intel

# Create virtual environment (one time only)
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies for all weeks
pip install -r requirements.txt
```

Then activate this same environment each time you work on the project:
```bash
source venv/bin/activate
```

---

## How to Run the Project

This section provides step-by-step instructions to run the entire threat intelligence platform. You will need 3 terminals: one for running Python scripts, one for MongoDB, and one for Docker services.

### Part 1: Initial Setup (Terminal 1)

Open your first terminal and set up the project:

```bash
# Navigate to project directory
cd Threat-Intel

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

Install dependencies for all weeks:

```bash
# Install Week1 dependencies
cd Week1
pip install -r requirements.txt

# Install Week2 dependencies
cd ../Week2
pip install -r requirements.txt

# Install Week3 dependencies
cd ../Week3
pip install -r requirements.txt

# Go back to main directory
cd ..
```

Your Terminal 1 is now ready. Keep it open.

### Part 2: Start MongoDB (Terminal 2)

Open a second terminal window. This terminal will run MongoDB.

```bash
# Start MongoDB service
sudo systemctl start mongod

# Check MongoDB status
sudo systemctl status mongod
```

You should see:
```
● mongod.service - MongoDB Database Server
   Loaded: loaded
   Active: active (running)
```

Leave Terminal 2 running with MongoDB active.

### Part 3: Start Elasticsearch and Kibana (Terminal 3)

Open a third terminal window. This terminal will run Docker services.

```bash
# Navigate to Week2 folder
cd Threat-Intel/Week2

# Start Elasticsearch and Kibana containers
docker-compose up -d

# Verify containers are running
docker-compose ps
```

You should see:
```
CONTAINER ID   IMAGE                        STATUS
xxx            docker.elastic.co/...        Up 2 minutes
yyy            docker.elastic.co/kibana...  Up 2 minutes
```

Services are running on:
- Elasticsearch: http://localhost:9200
- Kibana: http://localhost:5601

Leave Terminal 3 running.

### Part 4: Run the Project (Terminal 1)

Go back to your first terminal (Terminal 1 with Python scripts).

Activate the virtual environment if not already active:
```bash
source venv/bin/activate
```

#### Step 1: Run Week 1 (OSINT Collection)

```bash
cd Week1
python3 main.py
```

Wait for completion. You should see:
```
===== OSINT PIPELINE =====

Fetching OSINT data from sources...
  → Fetching from AlienVault OTX...
  → Fetching from VirusTotal...
  → Fetching from AbuseCH...
Total records fetched: 150

Cleaning data...
After cleaning: 145 records
After deduplication: 120 records

Storing data in MongoDB...
Database: Inserted 120 | Duplicates 0

Exporting data to files...
CSV exported → reports/threats.csv
JSON exported → reports/threats.json

===== PIPELINE COMPLETE =====
```

This fetches threat data from OSINT sources and stores it in MongoDB.

#### Step 2: Run Week 2 (Data Processing)

```bash
cd ../Week2
python3 pipeline.py
```

Wait for completion. You should see:
```
=== THREAT INTELLIGENCE PIPELINE ===

Step 1: Fetching data from MongoDB...
Found 120 records

Step 2: Normalizing data...
Normalized 120 records

Step 3: Applying scoring...
  192.168.1.10 - Risk: HIGH (Confidence: 95)
  45.33.32.156 - Risk: HIGH (Confidence: 88)

Step 4: Connecting to Elasticsearch...
Connected to Elasticsearch

Creating index...
Index created: threat-intel

Sending to Elasticsearch...
Inserted 120 documents

Pipeline completed
```

This processes the data and sends it to Elasticsearch.

#### Step 3: Run Week 3 (Policy Enforcement)

```bash
cd ../Week3
python3 policy_engine.py
```

The engine will start running continuously:
```
Starting Policy Engine
Checking MongoDB...
Found 45 high-risk IPs
Blocking IP: 192.168.1.10
Blocked IP: 192.168.1.10
Simulated block for IP: 45.33.32.156
Blocked IP: 45.33.32.156
Already blocked: 192.168.1.10
Checking MongoDB...
Found 45 high-risk IPs
```

Week 3 runs in a loop, checking MongoDB every 10 seconds. Press `Ctrl+C` to stop it.

---

## How to View Results

### View MongoDB Data

MongoDB stores data internally. To verify data was stored:

```bash
# In any terminal, use mongo command (if installed)
mongo threat_db
> db.indicators.count()
> db.indicators.findOne()
```

### View Elasticsearch Data

Open a browser and visit:
```
http://localhost:9200
```

You should see Elasticsearch status information.

### View Kibana Dashboard

Open a browser and visit:
```
http://localhost:5601
```

Steps to view your threat intelligence data:

1. Click on "Discover" in the left menu
2. Create a new index pattern: type `threat-intel`
3. Click "Create index pattern"
4. View your threat data in the main panel
5. You can create visualizations and dashboards here

### View Week 3 Output

Week 3 output appears in Terminal 1. You will see messages like:

- `Checking MongoDB...` - Connects to database
- `Found X high-risk IPs` - Number of threats detected
- `Blocking IP: 192.168.1.10` - Blocking action (simulated if SAFE_MODE=True)
- `Already blocked: 192.168.1.10` - Duplicate block prevention

If SAFE_MODE is True (default), these are simulated blocks. If SAFE_MODE is False, actual iptables rules are applied (requires sudo).

---

## Terminal Reference

Use this table to manage your three terminals:

| Terminal | Purpose | Command | Keeps Running |
|----------|---------|---------|----------------|
| Terminal 1 | Python scripts | `python3 main.py`, `python3 pipeline.py`, `python3 policy_engine.py` | No (except Week3) |
| Terminal 2 | MongoDB service | `sudo systemctl start mongod` | Yes |
| Terminal 3 | Elasticsearch/Kibana | `docker-compose up -d` | Yes |

**To stop services:**

Terminal 2: Press `Ctrl+C` or run `sudo systemctl stop mongod`

Terminal 3: Run `docker-compose down`

Terminal 1: Press `Ctrl+C` (only for Week3)

---

## Execution Order

Execute the weeks in this specific order. Each week builds on the previous week's data.

### Week 1: Collect OSINT Data

```bash
# From project root with virtual environment activated
cd Week1
python3 main.py
```

**What happens**:
- Fetches threat indicators from AlienVault OTX, VirusTotal, and AbuseCH
- Cleans and removes duplicates
- Stores data in MongoDB database (threat_db, collection: indicators)
- Exports to CSV and JSON files

**Output example**:
```
===== OSINT PIPELINE =====

Fetching OSINT data from sources...
  → Fetching from AlienVault OTX...
  → Fetching from VirusTotal...
  → Fetching from AbuseCH...
Total records fetched: 150

Cleaning data...
After cleaning: 145 records
After deduplication: 120 records

Storing data in MongoDB...
Database: Inserted 120 | Duplicates 0

Exporting data to files...
CSV exported → reports/threats.csv
JSON exported → reports/threats.json

===== PIPELINE COMPLETE =====
```

### Week 2: Process Data and Integrate with SIEM

First, start Elasticsearch and Kibana:
```bash
cd ../Week2

# Start Docker containers (Elasticsearch + Kibana)
docker-compose up -d

# Wait 30 seconds for containers to start
sleep 30
```

Then run the pipeline:
```bash
# Still in Week2 directory with virtual environment activated
python3 pipeline.py
```

**What happens**:
- Reads threat data from MongoDB
- Normalizes data to consistent format
- Applies risk scoring based on confidence values
- Sends enriched data to Elasticsearch
- Data becomes queryable in Kibana dashboard

**Output example**:
```
=== THREAT INTELLIGENCE PIPELINE ===

Step 1: Fetching data from MongoDB...
Found 120 records

Step 2: Normalizing data...
Normalized 120 records

Step 3: Applying scoring...
  192.168.1.10 - Risk: HIGH (Confidence: 95)
  8.8.8.8 - Risk: LOW (Confidence: 10)
  45.33.32.156 - Risk: HIGH (Confidence: 88)

Step 4: Connecting to Elasticsearch...
Connected to Elasticsearch

Creating index...
Index created: threat-intel

Sending to Elasticsearch...
Inserted 120 documents

Pipeline completed
```

**Access Kibana dashboard**:
- Open browser: http://localhost:5601
- View threat intelligence dashboard
- Create visualizations and alerts

### Week 3: Enforce Policy and Block IPs

```bash
cd ../Week3
python3 policy_engine.py
```

**What happens**:
- Connects to MongoDB and fetches all threat indicators
- Identifies high-risk IPs (risk="HIGH" OR confidence>=70)
- Attempts to block each IP using Linux firewall (iptables)
- Tracks already-blocked IPs to avoid duplicate blocking
- Runs continuously with 10-second checks

**Output example**:
```
Starting Policy Engine
Checking MongoDB...
Found 45 high-risk IPs
Blocking IP: 192.168.1.10
Blocked IP: 192.168.1.10
Simulated block for IP: 45.33.32.156
Blocked IP: 45.33.32.156
Already blocked: 192.168.1.10
Checking MongoDB...
Found 45 high-risk IPs
```

---

## Week 3: Dynamic Policy Enforcement Explained

### Overview

Week 3 automatically monitors your threat intelligence database and blocks malicious IPs in real-time. It demonstrates how organizations use threat intelligence to enforce security policies.

### How Week 3 Works

1. **Connect to MongoDB**
   - Reads threat indicators collected in Week 1 and enriched in Week 2

2. **Identify High-Risk Threats**
   - Queries for IPs with risk level "HIGH"
   - Queries for IPs with confidence >= 70%
   - Only high-confidence, high-risk threats are blocked

3. **Block Malicious IPs**
   - Uses `firewall.py` module to block IPs
   - Maintains a set of already-blocked IPs (prevents duplicate blocking)
   - Logs each blocking action to terminal

4. **Continuous Monitoring**
   - Runs in an infinite loop
   - Checks MongoDB every 10 seconds
   - Automatically blocks newly-detected high-risk IPs

### SAFE_MODE

Week 3 includes a SAFE_MODE safety feature:

**SAFE_MODE = True** (default):
- Simulates blocking without executing real iptables commands
- Safe for testing and learning
- Shows what would be blocked

**SAFE_MODE = False**:
- Actually blocks IPs using iptables
- Requires root privileges (sudo)
- Real firewall rules are enforced

To enable real blocking:
1. Edit `Week3/firewall.py`
2. Change `SAFE_MODE = False`
3. Run with sudo: `sudo python3 policy_engine.py`

---

## What You'll See

### After Week 1
- Terminal output showing data collection
- MongoDB contains threat indicators
- CSV and JSON files exported to `Week1/reports/`

### After Week 2
- Terminal output showing data processing
- Elasticsearch contains enriched threat data
- Kibana dashboard available at http://localhost:5601

### After Week 3
- Terminal output showing policy engine status
- Messages indicating which IPs are being blocked
- Messages showing "Already blocked" for repeated threats
- Real iptables rules if SAFE_MODE is disabled

---

## Important Requirements

Before running the project, ensure:

1. **MongoDB is running**
   ```bash
   sudo service mongodb start
   ```

2. **Docker services are running** (for Week 2 only)
   ```bash
   cd Week2
   docker-compose up -d
   ```

3. **Data dependency order**:
   - Week 3 requires data from Week 1 and Week 2
   - Always run Week 1 before Week 2
   - Always run Week 1 and Week 2 before Week 3

4. **Virtual environment is activated**
   ```bash
   source venv/bin/activate
   ```

---

## Troubleshooting

### MongoDB Connection Issues
```bash
# Start MongoDB
sudo service mongodb start

# Check status
sudo service mongodb status
```

### Elasticsearch Connection Issues
```bash
# Ensure docker-compose is running in Week2
cd Week2
docker-compose ps

# Restart if needed
docker-compose restart
```

### Import Errors
Ensure virtual environment is activated:
```bash
source venv/bin/activate
```

### Week 3 SAFE_MODE Not Blocking
If SAFE_MODE shows simulation messages but you need real blocking:
```bash
# Edit firewall.py to set SAFE_MODE = False
nano Week3/firewall.py

# Then run with sudo
sudo python3 policy_engine.py
```

---

## Learning Outcomes

By completing this project, you will understand:
- How to collect threat intelligence from multiple OSINT sources
- Data cleaning, validation, and normalization techniques
- Risk scoring methodologies for threat prioritization
- SIEM integration with Elasticsearch and Kibana
- Automated incident response and policy enforcement
- Firewall rule management in Linux systems

---

## Project Structure Summary

- **Week 1**: OSINT → Fetch → Clean → MongoDB storage
- **Week 2**: MongoDB → Normalize → Score → Elasticsearch indexing
- **Week 3**: MongoDB → Identify high-risk → Block → Track

Each week builds on previous data, creating an end-to-end threat intelligence platform.

---

## Documentation

For detailed information about each week:
- [Week1/README.md](Week1/README.md) - OSINT data collection
- [Week2/README.md](Week2/README.md) - Data processing and SIEM integration
- [Week3/README.md](Week3/README.md) - Policy enforcement and blocking
