import os
from dotenv import load_dotenv
from feeds.alienvault_otx import AlienVaultOTX
from feeds.virustotal import VirusTotal
from feeds.abusech import AbuseCH
from database import ThreatDB
from cleaner import clean_data, deduplicate
from exporter import Exporter

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
OTX_API = os.getenv("OTX_API_KEY", "")
VT_API = os.getenv("VIRUSTOTAL_API_KEY", "")


# STEP 1: FETCH DATA FROM MULTIPLE SOURCES
def fetch_all_data():
    print("Fetching OSINT data from sources...")
    
    data = []
    
    print("  → Fetching from AlienVault OTX...")
    otx = AlienVaultOTX(OTX_API)
    data += otx.fetch()
    
    print("  → Fetching from VirusTotal...")
    vt = VirusTotal(VT_API)
    data += vt.fetch()
    
    print("  → Fetching from AbuseCH...")
    abuse = AbuseCH()
    data += abuse.fetch()
    
    print(f"Total records fetched: {len(data)}")
    return data


# STEP 2: CLEAN AND DEDUPLICATE DATA
def clean_pipeline(data):
    print("Cleaning data...")
    cleaned = clean_data(data)
    print(f"After cleaning: {len(cleaned)} records")
    
    print("Removing duplicates...")
    unique = deduplicate(cleaned)
    print(f"After deduplication: {len(unique)} records")
    
    return unique


# STEP 3: STORE IN DATABASE
def store_in_database(data):
    print("Storing data in MongoDB...")
    db = ThreatDB()
    db.insert(data)
    db.close()


# STEP 4: EXPORT TO FILES
def export_data(data):
    print("Exporting data to files...")
    exporter = Exporter()
    exporter.to_csv(data)
    exporter.to_json(data)


def main():
    print("===== OSINT PIPELINE =====\n")
    
    # Step 1: Fetch
    raw_data = fetch_all_data()
    print()
    
    # Step 2: Clean
    cleaned_data = clean_pipeline(raw_data)
    print()
    
    # Step 3: Store
    store_in_database(cleaned_data)
    print()
    
    # Step 4: Export
    export_data(cleaned_data)
    print()
    
    print("===== PIPELINE COMPLETE ✅ =====")


if __name__ == "__main__":
    main()

