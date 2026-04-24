# Risk scoring based on confidence value

def calculate_risk(confidence):
    # Simple scoring based on confidence
    if confidence > 80:
        return "HIGH"
    elif confidence > 50:
        return "MEDIUM"
    else:
        return "LOW"


def add_risk_score(record):
    # Get confidence value (default 50 if missing)
    confidence = record.get("confidence", 50)
    
    # Calculate risk level
    risk = calculate_risk(confidence)
    
    # Add fields to record
    record["risk"] = risk
    record["confidence"] = confidence
    
    return record
