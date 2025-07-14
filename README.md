# 📋 Admin by Request (Unofficial Python SDK)

> **NOTE**  
> This project is **unofficial** and **not supported by Admin By Request (FastTrack Software)**.  
> Please do **not contact Admin By Request support** regarding issues with this SDK — open an issue on this repository instead.


This Python SDK provides an easy-to-use interface for interacting with the [Admin By Request Public API](https://www.adminbyrequest.com/en/docs/api-overview).  
It wraps the REST API into Pythonic classes and objects, providing clear data models and helper functions for Audit Logs, Inventory, Requests, Events, and PIN codes.

Primarily intended for proof-of-concept automation and integrations.  
🎯 Supports both EU (`dc1`) and US (`dc2`) datacenters.

---

## 📦 Requirements

- Python 3.8+
- [requests](https://pypi.org/project/requests/)

✅ Tested with:
- Python 3.11.4
- Python 3.12.3


Install dependencies:

```bash
pip install requests
```

## Outline

1. [Getting Started](#getting-started)
2. APIs
   - [Auditlog API](#auditlog-api-)
   - [Inventory API](#inventory-api-️)
   - [Request API](#requests-api-)
   - [Events API](#events-api-)
   - [Pincode API (WIP)](#pin-api-wip-)
3. [Admin by Request - Request Objects](#admin-by-request---request-objects)


## Getting Started

Example Setup:

```python
from adminbyrequest import AdminByRequest, ABRDatacenter

abr = AdminByRequest("YOUR_API_KEY", ABRDatacenter.dc2)  # US datacenter

# Fetch latest audit logs
logs = abr.get_auditlog(take=10)

for log in logs.values():
    print(log.user_account, log.status, log.application_name)

```

## Auditlog API 📖

This targets all the Auditlog API which includes 5 GET resources:

1. /auditlog - Returns an array of auditlog entries
2. /auditlog/[id] - Returns one auditlog entry by its ID
3. /computers/[computername]/auditlog - Returns an array of auditlog entries for a certain computer
4. /users/[user]/auditlog - Returns an array of auditlog entries for a certain user (user account of full name)
5. /auditlog/delta - Currently this only returns the timeNow value

### Audit functions

- `get_auditlog(...)` — Get all audit logs with optional filters (date range, status, type, etc.)
- `get_auditlog_id(id)` — Get a specific audit log by its ID
- `get_auditlog_computer(computername)` — Get audit logs for a specific computer
- `get_auditlog_username(username)` — Get audit logs for a specific user
- `get_auditlogs_delta(fullLog=False)` — Get the current timeNow delta (with optional full log)

Returns: ABRRequestAuditlogObject instances (or dict of them)

## Inventory API 🖥️

This targets all the Inventory API which includes 3 GET, and 2 DELETE resources:

**GET**

1. /inventory - Returns a full list of Inventory in your portal
2. /inventory/[id] - Returns a specfic Item from inventory by its ID value
3. /inventory/[computername] - Returns a specfic Item from inventory by its Computer Name value

**DELETE**

1. /inventory/[id] - Deletes Inventory Item by ID
2. /inventory/[computername] - Deletes Inventory Item by Computer Name

### Inventory functions

- `get_inventory(...)` - Get inventory list (all computers)
- `get_inventory_id(id)` - Get a computer by its inventory ID
- `get_inventory_computer(computername)` - Get a computer by its name
- `delete_inventory_id(id)` - Delete inventory item by ID
- `delete_inventory_computer(computername)` - Delete inventory item by name
- `get_inventory_by_date(days=30, unavailable=False)` - Get all inventory items that have not synced in X days or are unavailable

Returns: ABRRequestInventoryObject instances (or dict of them)

## Requests API 📝

This targets the Requests API which includes GET, PUT, and DELETE resources for managing elevation requests:

**GET**

1. /requests - Returns an array of elevation requests
2. /request/[id] - Returns one request entry by its ID

**PUT**

1. /request/[id] - Approves a request

**DELETE**

1. /request/[id] - Denies a request


### Request functions

- `get_requests(...)` — Get all pending/processed elevation requests
- `get_request_id(id)` — Get a specific request by ID
- `approve_request_id(id)` — Approve a request
- `approve_request_id_approvedby(id, approver)` — Approve a request and specify approver
- `deny_request_id(id)` — Deny a request
- `deny_request_id_reason(id, reason)` — Deny a request and specify reason
- `deny_request_id_deniedby(id, deniedby)` — Deny a request and specify who denied it
- `deny_request_id_reason_deniedby(id, deniedby, reason)` — Deny a request with both reason and who denied

Returns: `ABRRequestRequestsObject` instances (or dict of them)

## Events API 📊

This targets the Events API which includes GET resources for audit and system events:

**GET**

1. /events - Returns an array of all events
2. /events/[id] - Returns one event entry by its ID
3. /computers/[computername]/events - Returns events for a specific computer
4. /users/[username]/events - Returns events for a specific user
5. /events?code=[eventCode] - Returns events filtered by event code

### Event functions

- `get_events(...)` — Get all events
- `get_events_id(id)` — Get a specific event by ID
- `get_event_computer(computername)` — Get all events for a specific computer
- `get_events_user(username)` — Get all events for a specific user
- `get_events_errorCode(errorCode)` — Get all events filtered by event code

Returns: `ABRRequestEventObjects` instances (or dict of them)

## PIN API (WIP) 🔐

This targets the PIN Code API which provides one GET resource per computer:

**GET**

1. /inventory/[id]/pin - Returns the PIN code for a computer by its inventory ID
2. /inventory/[computername]/pin - Returns the PIN code for a computer by its name

### PIN functions

- `get_pin_id(id)` — Get PIN code for a computer by inventory ID
- `get_pin_computer(computername)` — Get PIN code for a computer by name

Returns: string PIN code

---

## **Examples**
 
 ### Delete Inventory (by Date) -
 Shows how you can set up an API that is designed to remove computers out of inventory after a set amount of days

 ### Get Auditlogs
 Shows how you can setup the all the auditlogs you would like, up to 10000 per request.
