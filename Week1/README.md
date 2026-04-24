# OSINT Threat Intelligence - Week 1

## Overview

Week 1 focuses on collecting threat data from multiple OSINT sources and storing it in MongoDB. This module demonstrates how to fetch information about malicious IP addresses from public sources, validate the data, and persist it to a database for later processing.

---

## What This Module Does

- Fetches threat intelligence data from multiple OSINT sources (AlienVault, VirusTotal, AbuseIPDB)
- Validates and cleans the data (IP format validation, duplicate detection)
- Stores validated data in MongoDB
- Exports results to CSV and JSON files

---

## Objectives

✅ Fetch data from multiple OSINT sources  
✅ Clean and validate IP addresses  
✅ Remove duplicate entries  
✅ Store data in MongoDB  

---

## Features

- **Multiple Data Sources** → Different OSINT feeds in the `feeds/` folder
- **Data Cleaning** → `cleaner.py` validates and removes duplicates
- **MongoDB Storage** → `database.py` handles all database operations
- **Pipeline** → `main.py` runs the whole process from start to finish

---

## How the Code is Organized

```
Week1/
├── main.py              ← Runs the entire pipeline
├── cleaner.py           ← Cleans data and removes duplicates
├── database.py          ← Stores data in MongoDB
├── exporter.py          ← Exports results to CSV and JSON
├── feeds/               ← OSINT data sources
│   ├── alienvault_otx.py
│   ├── virustotal.py
│   └── abusech.py
├── reports/             ← Output files (CSV and JSON)
├── templates/           ← HTML dashboard template (optional)
└── static/              ← CSS styling (optional)
```

### What Each File Does

| File | Purpose |
|------|---------|
| `main.py` | Starts the pipeline - fetches, cleans, stores, and exports |
| `cleaner.py` | Checks if IPs are valid and removes duplicates |
| `database.py` | Connects to MongoDB and saves data |
| `exporter.py` | Saves results to CSV and JSON files |
| `feeds/` | Contains code to fetch from AlienVault, VirusTotal, AbuseIPDB |

---

## How It Works

```
1. FETCH
   └─ Get threat data from all sources

2. COMBINE
   └─ Merge data from different feeds

3. CLEAN
   └─ Remove invalid IPs and duplicates

4. STORE
   └─ Save to MongoDB

5. EXPORT
   └─ Create CSV and JSON files
```

---

## Setup Instructions

### On Windows:

```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### On Linux/Mac:

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Run the Project

### Step 1: Start MongoDB
Make sure MongoDB is running on your computer (port 27017)

### Step 2: Run the Pipeline
```bash
python main.py
```

This will:
1. Fetch threat data from all sources
2. Clean and validate the data
3. Store it in MongoDB
4. Export results to `reports/threats.csv` and `reports/threats.json`

---

## What Gets Stored in MongoDB

Each threat entry has:
- **ip** → The malicious IP address
- **source** → Where it came from (AlienVault, VirusTotal, etc.)
- **timestamp** → When it was added
- **type** → Type of indicator (usually "ip")

---

## Files You'll Get

After running the pipeline, you'll have:
- `reports/threats.csv` → Spreadsheet format
- `reports/threats.json` → JSON format

---

## Notes

- **This is Week 1 only** - Week 1 focuses on data ingestion and storage
- **Week 2 builds on this** - Week 2 adds risk scoring and SIEM integration with Elasticsearch
- **API Keys** - Replace `YOUR_API_KEY` placeholders with actual API keys in `main.py`, or use a `.env` file for secure key management
- **Database Creation** - MongoDB database and collections are created automatically on first run
- **Dashboard** - The templates/ and static/ folders contain optional HTML UI components. The core functionality works without them.

---

## Troubleshooting

**MongoDB not connecting?**
- Make sure MongoDB is running
- Check that it's on localhost:27017

**Import errors?**
- Make sure you installed all requirements: `pip install -r requirements.txt`
- Make sure you're in the virtual environment

**No data fetched?**
- API keys might be missing (replace "YOUR_API_KEY" in main.py)
- Check your internet connection

---

## Next Steps

After Week 1 works, move to Week 2 to:
- Score threats by risk level
- Send data to Elasticsearch
- Visualize in Kibana

---
