# Simple data cleaning (kept for compatibility)
# For main cleaning pipeline, use cleaner.py instead

def clean_data(data):
    cleaned = []
    for item in data:
        if not item.get("indicator"):
            continue

        cleaned.append({
            "indicator": item["indicator"].strip(),
            "type": item.get("type", "unknown"),
            "source": item.get("source", "unknown"),
            "created": item.get("created")
        })

    return cleaned


def deduplicate(data):
    seen = {}
    for item in data:
        key = item["indicator"]
        if key not in seen:
            seen[key] = item
    return list(seen.values())

