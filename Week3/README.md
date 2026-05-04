# Week 3 - Dynamic Policy Enforcement Engine

## Overview

Week 3 focuses on building a **Dynamic Policy Enforcement Engine** that automatically enforces security policies based on threat intelligence data. The engine monitors threat indicators stored in MongoDB, evaluates them against configurable risk and confidence thresholds, and dynamically blocks high-risk IP addresses through firewall rules.

This module bridges threat intelligence data (from Weeks 1-2) with active network security enforcement, creating an automated response system to detected threats.

## Architecture

The Week 3 system consists of three main components working together:

```
┌─────────────────┐
│   MongoDB       │  (Threat Intelligence Database)
│  (Threat Data)  │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────┐
│   Policy Engine             │
│  (Intelligence Analysis)    │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│   Firewall Module           │
│  (Security Enforcement)     │
└─────────────────────────────┘
```

## Components

### 1. **config.py** - Configuration Management
Centralized configuration for the policy enforcement engine:

- **MongoDB Connection**: `MONGO_URI` - Connection string to MongoDB instance
- **Database Settings**: 
  - `DB_NAME` - Database name ("threat_db")
  - `COLLECTION_NAME` - Collection for threat indicators
- **Threat Thresholds**:
  - `RISK_THRESHOLD` - Minimum risk level to trigger action (default: "HIGH")
  - `CONFIDENCE_THRESHOLD` - Minimum confidence score 0-100 (default: 70)
- **Engine Parameters**:
  - `SLEEP_TIME` - Delay between policy checks (seconds)
  - `MAX_RUNS` - Maximum number of enforcement cycles

### 2. **policy_engine.py** - Core Enforcement Logic
The main policy enforcement engine that:

- **Connects to MongoDB**: Retrieves threat intelligence indicators
- **Risk Assessment**: Evaluates indicators against risk and confidence thresholds
- **IP Identification**: Extracts high-risk IPs from threat data
- **Enforcement Loop**: Continuously monitors and enforces policies
- **Duplicate Prevention**: Tracks already-blocked IPs to avoid redundant actions

Key Functions:
- `connect_db()` - Establishes MongoDB connection
- `get_high_risk_ips()` - Filters indicators meeting threat criteria
- `run_policy_engine()` - Main enforcement loop

### 3. **firewall.py** - Firewall Interface
Handles IP blocking with safe mode support:

- **Safe Mode**: Simulates blocking for testing/development
- **Production Mode**: Uses `iptables` for actual network enforcement
- Provides a consistent interface for IP blocking operations

## Installation

### Prerequisites
- Python 3.7+
- MongoDB instance running locally or remotely
- Linux system (for iptables support)
- `sudo` privileges (for production firewall rules)

### Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure MongoDB connection in `config.py`:
```python
MONGO_URI = "mongodb://localhost:27017/"  # Update if needed
```

3. Set risk thresholds based on your security requirements:
```python
RISK_THRESHOLD = "HIGH"        # "LOW", "MEDIUM", "HIGH", "CRITICAL"
CONFIDENCE_THRESHOLD = 70      # 0-100
```

4. Enable/disable safe mode in `firewall.py`:
```python
SAFE_MODE = True   # Set to False for production enforcement
```

## Usage

### Running the Policy Engine

```bash
python policy_engine.py
```

The engine will:
1. Connect to MongoDB
2. Query threat indicators matching your configuration
3. Block identified high-risk IPs every `SLEEP_TIME` seconds
4. Continue for `MAX_RUNS` iterations

### Example Output

```
Starting Policy Engine
Checking MongoDB...
Found 5 high-risk IPs
Simulated block for IP: 192.168.1.100
Blocked IP: 192.168.1.100
Simulated block for IP: 10.0.0.50
Blocked IP: 10.0.0.50
...
```

## Features

- **Automated Threat Response**: Automatically blocks threats without manual intervention
- **Configurable Thresholds**: Set custom risk and confidence requirements
- **Database Integration**: Reads from MongoDB threat intelligence collection
- **Safe Mode Testing**: Test policies without affecting network traffic
- **Scalable Design**: Can be extended for additional enforcement methods
- **Logging Output**: Clear status messages for monitoring and debugging

## Configuration Options

### Risk Levels
The engine recognizes standard risk classifications:
- `LOW` - Minimal security concern
- `MEDIUM` - Moderate threat level
- `HIGH` - Significant security risk
- `CRITICAL` - Immediate threat requiring action

### Threshold Strategy

Set thresholds based on your security posture:

| Security Level | RISK_THRESHOLD | CONFIDENCE_THRESHOLD |
|---|---|---|
| Permissive | MEDIUM | 50 |
| Balanced | HIGH | 70 |
| Strict | CRITICAL | 85 |

## Integration with Previous Weeks

- **Week 1**: Threat intelligence feeds populate MongoDB with indicators
- **Week 2**: Normalized and scored threat data with confidence scores
- **Week 3**: Enforcement engine acts on intelligence from Weeks 1-2

## Future Enhancements

- Multi-firewall support (pf, Windows Firewall, cloud WAF)
- Policy rollback mechanisms
- Detailed audit logging
- REST API for policy management
- Advanced threat correlation
- Geographic-based blocking policies
- Time-based enforcement windows

## Testing

To test the policy engine safely:

1. Ensure `SAFE_MODE = True` in `firewall.py`
2. Insert test threat indicators into MongoDB
3. Run the engine and verify output
4. Review blocked IPs without network impact

## Production Deployment

Before production:

1. Set `SAFE_MODE = False` in `firewall.py`
2. Verify MongoDB connectivity and data
3. Test with non-critical IP ranges first
4. Run with appropriate `MAX_RUNS` for continuous operation
5. Implement monitoring and alerting
6. Establish rollback procedures
