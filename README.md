# AdminByRequest (Unofficial Python Package)

Feel free to use this for your projects if you are developing things with the Admin by Request API. I mostly use this to show proof of concepts of all that is available with the API. This project is still a work in progress so sorry if everything isn't available yet. This is not associated with the Admin by Request company and contains nothing special outside of the already available Public API documented at [Public API &gt;  API Overview](https://www.adminbyrequest.com/en/docs/api-overview)

## Outline
- Required
- Getting Started
- Functions

### Required
python (tested on version 3.11.4)
#### Packages
- requests

### Getting Started
Example Setup:
```python
from adminbyrequest import AdminByRequest, ABRDatacenter # AdminByRequest is the function class, ABRDataCenter is for Enums

abr = AdminByRequest(APIKEY, ABRDatacenter.dc2) #API and What Datacenter (dc1 = EU, dc2 = US)

abr.get_auditlog(limit = 50)
#Returns the First 50 auditlog reports in JSON
```

### Functions

#### Auditlog API:

This targets all the Auditlog API which includes 5 GET resources:

1. /auditlog - Returns an array of auditlog entries
2. /auditlog/[id] - Returns one auditlog entry by its ID
3. /computers/[computername]/auditlog - Returns an array of auditlog entries for a certain computer
4. /users/[user]/auditlog - Returns an array of auditlog entries for a certain user (user account of full name)
5. /auditlog/delta - Currently this only returns the timeNow value

##### GET Methods -

###### **Get all the Auditlogs** - This just returns all available auditlogs in JSON Format
This grabs all of the Auditlogs up to 10000 if you are over that or want to modify that value simply change the parameters

- limit(optional) = default is 10000 which is the max ABR can handle in 1 request
- offset(optional) = default is 0 but this will change where the record starts so if you have more than Admin by Request 10000 limit, you can use offset to handle Pagination
```python
# The function
def get_auditlog(self, limit:int = 10000, offset: int=0):
        return auditlogs
# Returns
# {
#           "installs": [],
#           "uninstalls": [
#               {
#                   "application": "Admin By Request Workstation",
#                   "version": "8.3.1.0",
#                   "vendor": "FastTrack Software"
#               }
#           ],
#           "elevatedApplications": [
#               {
#                   "name": "Admin By Request Workstation",
#                   "path": "Z:\\Downloads",
#                   "file": "Admin By Request 8.3.msi",
#                   "version": "8.4.0.0",
#                   "vendor": "Admin By Request ApS",
#                   "sha256": "420asdfasdfasdfBlaze6d5f41s62It",
#                   "scanResult": "Clean",
#                   "scanResultCode": 0,
#                   "threat": null,
#                   "virustotalLink": "https://www.virustotal.com/latest-scan/420asdfasdfasdfBlaze6d5f41s62It"
#               }
#           ],
#           "scanResults": [],
#           "id": 95423844,
#           "traceNo": "76136610",
#           "settingsName": "Global",
#           "type": "Run As Admin",
#           "typeCode": 0,
#           "status": "Finished",
#           "statusCode": 2,
#           "application": {
#               "file": "Admin By Request 8.3.msi",
#               "path": "Z:\\Downloads",
#               "name": "Admin By Request Workstation",
#               "vendor": "Admin By Request ApS",
#               "version": "8.4.0.0",
#               "sha256": "420asdfqwemnAasdfBl666aze6d5f41s62It",
#               "scanResult": "Clean",
#               "scanResultCode": 0,
#               "threat": null,
#               "virustotalLink": "https://www.virustotal.com/latest-scan/420asdftutkfcasddfBlaze6d5f41s62It",
#               "preapproved": false
#           },
#           "user": {
#               "account": "AZUREAD\\DPerson",
#               "fullName": "David Person",
#               "email": "test@test.com",
#               "phone": "1555555555",
            },
#               "isAdmin": true
#           "computer": {
#               "name": "ABR0234",
#               "platform": "Windows",
#               "platformCode": 0,
#               "make": "VMware, Inc.",
#               "model": "VMware20,1"
#           },
#           "reason": null,
#           "approvedBy": null,
#           "approvedByEmail": null,
#           "deniedReason": null,
#           "deniedBy": null,
#           "deniedByEmail": null,
#           "ssoValidated": false,
#           "requestTime": "2024-01-31T15:40:06",
#           "requestTimeUTC": "2024-01-31T20:40:06",
#           "startTime": "2024-01-31T15:40:06",
#           "startTimeUTC": "2024-01-31T20:40:06",
#           "endTime": "2024-01-31T15:40:23",
#           "endTimeUTC": "2024-01-31T20:40:23",
#           "responseTime": null,
#           "auditlogLink": "https://www.adminbyrequest.com/AuditLog?Page=AppElevations&ID=76136610&ShowFilter=false"
#       }, #... and so on
```


###### **Get the Auditlog by it's ID** - Returns one Auditlog

```python
def get_auditlog_id(id=95423844):
	returns auditlog_id

# Returns only the auditlogs matching the ID
```

###### **Get the Auditlog by it's Computer Name** - Returns auditlogs from Computer Name

```python
def get_auditlog_id(computername='USCORPWIN11'):
	returns auditlog_id

# Returns only the auditlogs with the computer name
```

###### **Get the Auditlog by the User** - Returns auditlogs from Username

```python
def get_auditlog_username(username='davidap'):
	returns auditlog_id

# Returns only the auditlogs from the user with username
```

###### **Get the Auditlog Delta** - Returns the Delta
To enable the full report for Auditlog Delta change fullLog to True

```python
def get_auditlog_id(fulllog: bool=False):
	returns auditlog_id

# Returns Delta time w/ or w/o Auditlog
```

#### Inventory API:
This targets all the Inventory API which includes 3 GET, and 2 DELETE resources:

**GET**
1. /inventory - Returns a full list of Inventory in your portal
2. /inventory/[id] - Returns a specfic Item from inventory by its ID value
3. /inventory/[computername] - Returns a specfic Item from inventory by its Computer Name value

**DELETE**
1. /inventory/[id] - Deletes Inventory Item by ID
2. /inventory/[computername] - Deletes Inventory Item by Computer Name

##### GET Methods -

###### **Get all Inventory** - Returns all the inventory in JSON Format
By default this method grabs all computers in inventory up to 10000 if you are over that or want to modify that value simply change the parameters

- limit(optional) = default is 10000 which is the max ABR can handle in 1 request
- offset(optional) = default is 0 but this will change where the record starts so if you have more than Admin by Request 10000 limit, you can use offset to handle Pagination

```python
# The function
def get_inventory(limit: int=10000, offset: int=0):
        return get_inventory
# Returns
#[
#  {
#    "id": 51342264,
#    "name": "COMPUTERNAME",
#    "inventoryAvailable": true,
#    "inventoryDate": "2024-08-27T14:04:14.887",
#    "abrClientVersion": "8.4.0",
#    "abrClientInstallDate": "2024-08-27T13:27:40",
#    "notes": null,
#    "user": {
#      "account": "davidap",
#      "fullName": "David A. Person",
#      "email": null,
#      "phone": null,
#      "isAdmin": false,
#      "domain": "ABR-Domain",
#      "isDomainJoined": true,
#      "isAzureJoined": false,
#      "orgUnit": "Users",
#      "orgUnitPath": "\\Users",
#      "groups": null
#    },
#    "owner": {
#      "account": "LOCAL-DAVID",
#      "fullName": "David"
#    },
#    "computer": {
#      "domain": "ABR-DOMAIN",
#      "isDomainJoined": true,
#      "isAzureJoined": true,
#      "orgUnit": "PROD",
#      "orgUnitPath": "\\TEST\\PROD",
#      "groups": null,
#      "localAdmins": [
#        "ABR-DOMAIN\\davidap-abr",
#        "ABR-DOMAIN\\Domain Admins",
#        "Admin",
#        "Administrator",
#        "AzureAD\\Company Administrators",
#        "AzureAD\\Device Administrators",
#        "S-1-12-1-4072261373-1340022675-2907612035-1391370097"
#      ],
#      "users": []
#    },
#    "operatingSystem": {
#      "platform": "Windows",
#      "platformCode": 0,
#      "name": "Windows 11 Pro",
#      "version": "23H2",
#      "release": 2009,
#      "build": 22631,
#      "buildUpdate": 4037,
#      "type": "Workstation",
#      "typeCode": 0,
#      "bits": 64,
#      "installDate": "2023-09-18T00:00:00"
#    },
#    "hardware": {
#      "make": "VMware, Inc.",
#      "model": "VMware20,1",
#      "type": "Desktop",
#      "typeCode": 1,
#      "serviceTag": "asdfas;ldkfjas",
#      "cpu": "12th Gen Intel Core i7-12700H",
#      "cpuSpeed": 2688,
#      "cpuCores": 4,
#      "diskSize": 136,
#      "diskFree": 63,
#      "diskStatus": "OK",
#      "memory": 4293,
#      "noMonitors": 1,
#      "monitorResolution": "1024x768",
#      "bitlockerEnabled": false,
#      "isCompliant": false,
#      "tpmEnabled": true,
#      "tpmVersion": "2.0"
#    },
#    "network": {
#      "publicIP": "[PUBLICIP]",
#      "privateIP": "[PRIVATEIP]",
#      "macAddress": "[MACADDRESS]",
#      "nicSpeed": "1000 mbit",
#      "hostName": null
#    },
#    "location": {
#      "city": "New York City",
#      "region": "New York",
#      "country": "United States",
#      "latitude": "0",
#      "longitude": "0",
#      "googleMapsLink": "https://maps.google.com/?q=43.064800,-88.094500",
#      "hourOffset": -6
#    },
#    "software": null
#  }
#]
```
###### **Get Inventory by ID** - Returns the computer by ID

```python
# The function
def get_inventory_id(id):
        return get_inventory

# Returns only the computer with the matching ID
```

###### **Get Inventory by Computer Name** - Returns the computer by Computer Name

```python
# The function
def get_inventory_id(computername):
        return get_inventory

# Returns only the computer with the matching computer name
```

###### **Delete Inventory by ID** - Deletes the computer from Inventory by ID

```python
# The function
def delete_inventory_id(id):
       
# Delete's Item by ID
```

###### **Delete Inventory by Computer Name** - Deletes the computer from Inventory by Computer Name

```python
# The function
def delete_inventory_computer(computername):
       
# Delete's Item by Computer Name
```

###### **Get All Inventory Items Older than X Amount of Days** - Returns as a object where you can pull specic data components
This function is a special function designed to show how you can setup your own inactivity deleting tool with the API, you may need to use a combination of this and then you can use the Delete by ID or Computer Name function

**What it currently grabs**
- id: Returns the ID's
- name: Returns the Computer Name
- inventoryDate: Returns last Inventory Sync
- inventoryAvailable: Returns if the Computer is Available (This will always be true if unavailable parameter is set False)
- abrClientVersion: Returns Version of Admin By Request installed
- operatingSystem: Returns OS of Computer

**Parameters**
1. days - How many days back Minimum since laster Inventory Time (30 would be any computer that hasn't sync'd in a month)
2. limit - the Max amount of records to return, by default its 10000
3. unavailable - by default this is false and therefore won't return any items outside of inventory

