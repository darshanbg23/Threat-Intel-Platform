# Week 4: Rollback & Testing

## What This Week Does

Provides rollback mechanism to unblock previously blocked IPs and includes a test suite to verify the complete blocking/rollback workflow.

## How to Run

```bash
cd Week4
python3 test_week4.py
```

## Expected Output

```
Starting Week4 Tests
Inserted test IP: 10.0.0.50

Test 1: Blocking successful
Test 2: Rollback successful

Tests completed
```

## Files

- `rollback.py` - Unblock IPs and update MongoDB (blocked = False)
- `test_week4.py` - Test suite that inserts, blocks, unblocks, and cleans up test data

## How to Use Rollback

Edit `rollback.py` to change the target IP:

```python
ip = "YOUR_IP_HERE"  # Change this
unblock_ip(ip)
```

Then run:
```bash
python3 rollback.py
```

## Notes

- Requires MongoDB running
- Requires Week1, Week2, Week3 data to exist
- SAFE_MODE applies (simulates unblock by default, same as Week3)
- Updates MongoDB: sets blocked = False, action = "unblocked"
