# Data normalization - ensure consistent format

def normalize_record(record):
    # Ensure required fields: ip, source, timestamp
    normalized = {
        "ip": record.get("ip", "").strip() if record.get("ip") else "",
        "source": record.get("source", "").strip() if record.get("source") else "unknown",
        "timestamp": record.get("timestamp", ""),
    }
    
    # Include other fields
    if "threat" in record:
        normalized["threat"] = record.get("threat", "").lower()
    
    if "confidence" in record:
        normalized["confidence"] = record.get("confidence", 50)
    
    # Validate - ip must exist
    if not normalized["ip"]:
        return None
    
    return normalized


def normalize_data(records):
    # Normalize all records
    normalized_records = []
    
    for record in records:
        normalized = normalize_record(record)
        if normalized:
            normalized_records.append(normalized)
    
    print(f"Normalized {len(normalized_records)} records")
    return normalized_records
