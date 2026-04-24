import re

# Check if string is valid IPv4
def is_valid_ipv4(ip):
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(ipv4_pattern, ip):
        return False
    
    parts = ip.split('.')
    for part in parts:
        num = int(part)
        if num < 0 or num > 255:
            return False
    
    return True


# Check if string is valid IPv6
def is_valid_ipv6(ip):
    ipv6_pattern = r'^(([0-9a-fA-F]{0,4}:){2,7}[0-9a-fA-F]{0,4}|::)$'
    return re.match(ipv6_pattern, ip) is not None


# Check if indicator is a valid IP (IPv4 or IPv6)
def is_valid_ip(indicator):
    if not indicator or not isinstance(indicator, str):
        return False
    
    indicator = indicator.strip()
    
    if is_valid_ipv4(indicator):
        return True
    
    if is_valid_ipv6(indicator):
        return True
    
    return False


# Clean and filter valid IPs
def clean_data(data):
    cleaned = []
    
    for item in data:
        if not isinstance(item, dict):
            continue
        
        indicator = item.get("indicator")
        
        if not is_valid_ip(indicator):
            continue
        
        indicator = indicator.strip()
        
        cleaned_item = {
            "ip": indicator,
            "source": item.get("source", "unknown"),
            "timestamp": item.get("created")
        }
        
        cleaned.append(cleaned_item)
    
    return cleaned


# Remove duplicate IPs using set
def deduplicate(data):
    seen = set()
    unique = []
    
    for item in data:
        ip = item.get("ip")
        
        if ip not in seen:
            seen.add(ip)
            unique.append(item)
    
    return unique

