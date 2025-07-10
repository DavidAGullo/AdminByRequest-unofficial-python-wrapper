# **IMPORTANT**

All issues with the script should be posted here, not with Admin By Request, Admin By Request does not officially support this project, nor any other API tool outside of their Integrations.

# AdminByRequest (Unofficial Python Package)

Feel free to use this for your projects if you are developing things with the Admin by Request API. I mostly use this to show proof of concepts of all that is available with the API. This project is still a work in progress so sorry if everything isn't available yet. This is not associated with the Admin by Request company and contains nothing special outside of the already available Public API documented at [Public API &gt;  API Overview](https://www.adminbyrequest.com/en/docs/api-overview)

## Outline

1. [Required](#required)
   - [Package(s)](#packages)
2. [Getting Started](#getting-started)
3. [Functions](#functions)
   - [Auditlog API](#auditlog-api)
   - [Inventory API](#inventory-api)
4. [Admin by Request - Request Objects](#admin-by-request---request-objects)

## Required

**Python**

* 3.8+ (no tested)

**Tested Python Version(s)**

- Version 3.11.4
- Version 3.12.3

#### Package(s)

- [requests](https://pypi.org/project/requests/)

## Getting Started

Example Setup:

```python
from adminbyrequest import AdminByRequest, ABRDatacenter # AdminByRequest is the function class, ABRDataCenter is for Enums

abr = AdminByRequest(APIKEY, ABRDatacenter.dc2) #API and What Datacenter (dc1 = EU, dc2 = US)

abr.get_auditlog(limit = 50)
#Returns the First 50 auditlog reports
```

## Functions

#### Auditlog API:

This targets all the Auditlog API which includes 5 GET resources:

1. /auditlog - Returns an array of auditlog entries
2. /auditlog/[id] - Returns one auditlog entry by its ID
3. /computers/[computername]/auditlog - Returns an array of auditlog entries for a certain computer
4. /users/[user]/auditlog - Returns an array of auditlog entries for a certain user (user account of full name)
5. /auditlog/delta - Currently this only returns the timeNow value

##### GET Methods -

###### **Get all the Auditlogs** - This just returns all available auditlogs in Object Format

This grabs all of the Auditlogs up to 10000 if you are over that or want to modify that value simply change the parameters

- limit(optional) = default is 10000 which is the max ABR can handle in 1 request
- offset(optional) = default is 0 but this will change where the record starts so if you have more than Admin by Request 10000 limit, you can use offset to handle Pagination

```python
# The function
def get_auditlog(self, limit:int = 10000, offset: int=0):
        return auditlog[]
# No longer returns a JSON but instead an object with all the values
```

###### **Get the Auditlog by it's ID** - Returns one Auditlog

```python
def get_auditlog_id(id=95423844):
	returns auditlog

# Returns only the auditlogs matching the ID
```

###### **Get the Auditlog by it's Computer Name** - Returns auditlogs from Computer Name

```python
def get_auditlog_id(computername='USCORPWIN11'):
	returns auditlog

# Returns only the auditlogs with the computer name
```

###### **Get the Auditlog by the User** - Returns auditlogs from Username

```python
def get_auditlog_username(username='davidap'):
	returns auditlog

# Returns only the auditlogs from the user with username
```

###### **Get the Auditlog Delta** - Returns the Delta

To enable the full report for Auditlog Delta change fullLog to True

```python
def get_auditlog_delta(fulllog: bool=False):
	returns auditlog['timeNow']
# Returns Delta time w/ or w/o Auditlog 
# Returns as JSON
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

###### **Get all Inventory** - Returns all the inventory in Object Format

By default this method grabs all computers in inventory up to 10000 if you are over that or want to modify that value simply change the parameters

- limit(optional) = default is 10000 which is the max ABR can handle in 1 request
- offset(optional) = default is 0 but this will change where the record starts so if you have more than Admin by Request 10000 limit, you can use offset to handle Pagination

```python
# The function
def get_inventory(limit: int=10000, offset: int=0):
        return get_inventory[]
# No longer returns a JSON but instead an object with all the values
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

To grab the a value simply call the function and define the properties as needed.

**Example:**

```python
from adminbyrequest import AdminByRequest, ABRDatacenter

abr = AdminByRequest(APIKEY, ABRDatacenter.dc2) #US

value = abr.get_inventory_by_date(30) # Inventory Sync date was 30 days ago 

for item in value:
	print(value[item].name)

# WIN11BOBT
# WIN11JOHND
# WIN11JOHNT
# ...
```

**This will grab everything now, here is a full list (these will fully be covered later: here)**

- .id: returns ID for the Inventory, may be used for deleting or referencing specifically for other requests.
- .name: gives Inventory's computer name, can also be used to delete or reference specifically for other requests
- .inventoryAvailable: Is the inventory available (By default this will alwyas be True; if you enable unavailable parameter this may show other results)
- .inventoryDate: This will return the value of the last inventory sync (I wouldn't recommend doing anything less than 14 days as some machines may not sync for multiple days and this can be attributed to a few reasons, and this is expected behavior)
- .clientVersion - Version of Admin by Request Installed
- .clientInstall - When Admin by Request was Installed
- .notes - notes for the computer
- .user_account - The user's account name
- .user_fullname - The user's Full Name according to OS
- .user_email - The user's email according to OS
- .user_phone - The user's phone number according to OS
- .user_isAdmin - Is this user (current user) an admin?
- .user_domain - The domain the User is connected to (requires machine to be connected to Domain)
- .user_isdomainjoined - Is this machine domain joined
- .user_isAzureJoined - Is this machine joined to a Azure Domain
- .user_orgUnit - The Orgizational Unit the user belongs to
- .user_orgUnitPath - The path to the Organziational Unit the user belongs to
- .user_groups - An array of groups the user belongs to
- .owner_account - Defines the computer owner of user's account name
- .owner_fullname - Defines the computer owner of user's full name
- .computer_domain - Computer's Domain
- .computer_domainjoined - Is the computer domain joined?
- .computer_isAzureJoined - Is it Azure Joined?
- .computer_orgUnit - Computers Organizational Unit
- .computer_orgUnitPath - Is the Organizational Unit's PAth
- .computer_groups - An array of groups the computer belongs to
- .computer_localAdmins - An array of Local Admin's on the computer
- .computer_users - An array of users on the machine
- .os_platform - Operating System's Platform Name (Windows, Apple, etc.)
- .os_plaformCode - ...
- .os_name - Operating System's Version name (Windows 11 Pro, macOS 14.5, etc.)
- .os_version - Operating System's Version Specific (23H2, Version 14.5 (Build 23F79))
- .os_release - ...
- .os_build - Build number
- .os_buildUpdate - ...
- .os_type - Windows specific item that determines what type of Windows its operating with, such as Workstation and Server
- .os_typeCode - ...
- .os_bits - Operating System Architecture (64 bit)
- .os_installDate - When was the OS installed
- .hardware_make - Brand that makes the computer
- .hardware_model - Computer Model
- .hardware_type - Computer is a Portable or Desktop
- .hardware_typeCode - ...
- .hardware_serviceTag - The Service Tag for the computer
- .hardware_CPU - CPU Name
- .hardware_CPUspeed - Clock speed of cpu
- .hardware_CPUcores - How many cores does the device have
- .hardware_diskSize - How big is the Storage Disk
- .hardware_diskFree - How much space is free on the Storage Disk
- .hardware_diskStatus - Storage is Online
- .hardware_memory - RAM Capacity
- .hardware_noMonitors - Number of Monitors connected
- .hardware_monitorResolution - Main monitor Resolution
- .hardware_bitlockerStatus - Is Bitlocker Enabled?
- .hardware_isCompliant - Is Intune Compliant?
- .hardware_tpmEnabled - TPM Enabled?
- .hardware_tpmVersion - TPM Version
- .network_publicIP - Public IP Address
- .network_privateIP - Private IP Address
- .network_mac - Devices MAC Address
- .network_nicSpeed - NIC Speed
- .network_hostname - Network's Hostname
- .location_city - Geolocation for the City the Device is located
- .location_region - Geolocation for the Region/State where the device is located
- .location_country - Geolocation for the Country its located
- .location_latitude - Geolocation Latitude
- .location_longitude - Geolocation Longitude
- .googleMaps - Provide's the link to the Google Maps location
- .hourOffset - Hours offset from UTC +0
- .software - An Array. (Empty)

**Parameters**

1. days - How many days back Minimum since laster Inventory Time (30 would be any computer that hasn't sync'd in a month)
2. limit - the Max amount of records to return, by default its 10000
3. unavailable - by default this is false and therefore won't return any items outside of inventory

## Admin by Request - Request Objects

### Summary

This basically transform the json format to a much easier format to call and organize with, these are special objects I've added for this purpose

##### ABRRequestInventoryObject

- .id: returns ID for the Inventory, may be used for deleting or referencing specifically for other requests.
- .name: gives Inventory's computer name, can also be used to delete or reference specifically for other requests
- .inventoryAvailable: Is the inventory available
- .inventoryDate: This will return the value of the last inventory sync (I wouldn't recommend doing anything less than 14 days as some machines may not sync for multiple days and this can be attributed to a few reasons, and this is expected behavior)
- .clientVersion - Version of Admin by Request Installed
- .clientInstall - When Admin by Request was Installed
- .notes - notes for the computer
- .user_account - The user's account name
- .user_fullname - The user's Full Name according to OS
- .user_email - The user's email according to OS
- .user_phone - The user's phone number according to OS
- .user_isAdmin - Is this user (current user) an admin?
- .user_domain - The domain the User is connected to (requires machine to be connected to Domain)
- .user_isdomainjoined - Is this machine domain joined
- .user_isAzureJoined - Is this machine joined to a Azure Domain
- .user_orgUnit - The Orgizational Unit the user belongs to
- .user_orgUnitPath - The path to the Organziational Unit the user belongs to
- .user_groups - An array of groups the user belongs to
- .owner_account - Defines the computer owner of user's account name
- .owner_fullname - Defines the computer owner of user's full name
- .computer_domain - Computer's Domain
- .computer_domainjoined - Is the computer domain joined?
- .computer_isAzureJoined - Is it Azure Joined?
- .computer_orgUnit - Computers Organizational Unit
- .computer_orgUnitPath - Is the Organizational Unit's PAth
- .computer_groups - An array of groups the computer belongs to
- .computer_localAdmins - An array of Local Admin's on the computer
- .computer_users - An array of users on the machine
- .os_platform - Operating System's Platform Name (Windows, Apple, etc.)
- .os_plaformCode - ...
- .os_name - Operating System's Version name (Windows 11 Pro, macOS 14.5, etc.)
- .os_version - Operating System's Version Specific (23H2, Version 14.5 (Build 23F79))
- .os_release - ...
- .os_build - Build number
- .os_buildUpdate - ...
- .os_type - Windows specific item that determines what type of Windows its operating with, such as Workstation and Server
- .os_typeCode - ...
- .os_bits - Operating System Architecture (64 bit)
- .os_installDate - When was the OS installed
- .hardware_make - Brand that makes the computer
- .hardware_model - Computer Model
- .hardware_type - Computer is a Portable or Desktop
- .hardware_typeCode - ...
- .hardware_serviceTag - The Service Tag for the computer
- .hardware_CPU - CPU Name
- .hardware_CPUspeed - Clock speed of cpu
- .hardware_CPUcores - How many cores does the device have
- .hardware_diskSize - How big is the Storage Disk
- .hardware_diskFree - How much space is free on the Storage Disk
- .hardware_diskStatus - Storage is Online
- .hardware_memory - RAM Capacity
- .hardware_noMonitors - Number of Monitors connected
- .hardware_monitorResolution - Main monitor Resolution
- .hardware_bitlockerStatus - Is Bitlocker Enabled?
- .hardware_isCompliant - Is Intune Compliant?
- .hardware_tpmEnabled - TPM Enabled?
- .hardware_tpmVersion - TPM Version
- .network_publicIP - Public IP Address
- .network_privateIP - Private IP Address
- .network_mac - Devices MAC Address
- .network_nicSpeed - NIC Speed
- .network_hostname - Network's Hostname
- .location_city - Geolocation for the City the Device is located
- .location_region - Geolocation for the Region/State where the device is located
- .location_country - Geolocation for the Country its located
- .location_latitude - Geolocation Latitude
- .location_longitude - Geolocation Longitude
- .googleMaps - Provide's the link to the Google Maps location
- .hourOffset - Hours offset from UTC +0
- .software - An Array. (Empty)

##### ABRRequestAuditlogObject

- .installs - An array that captures what was installed
- .uninstalls - An array that captures what was uninstalled
- .elevatedApplications - An array that captures what application was elevated
- .scanResults - An array that captures the scanResults
- .id: int - Auditlog ID
- .traceNo - The trace number for the Auditlog Request
- .settingsName -  Global or Subsetting Name
- .runType - 'Run As Admin', 'Admin Session'
- .typeCode -  ...
- .status - "Pending", "Finished"
- .statusCode - ...
- .application_file - Application File Name
- .application_path - Application Path location
- .application_name - Application's Name
- .application_vendor - Application's Vendor
- .application_version - Application's Version
- .application_sha256 - Application's SHA256 Checksum
- .application_scanResult - Application's Virus total results
- .application_scanResultCode - ...
- .application_threat - ...
- .application_virustotalLink - The URL to the VirusTotal Report
- .application_preapproved - Was application pre-approved?
- .user_account - Request's User's Account
- .user_fullname - The User's Full name
- .user_email - The User's Email
- .user_phone - The User's Phone Number
- .user_isAdmin - Is the User an Admin?
- .computer_name - Computer name
- .computer_platform - Computer's Platform (Windows, Apple)
- .computer_platformCode - ...
- .computer_make - Computers Make
- .computer_model - Computers Model
- .reason - The reason the user gave for the application
- .approvedBy - Who approved it in the portal (requires the user approve from the portal)
- .approvedByEmail - The approver's email (requires the user approve from the portal)
- .deniedReason - Reason the request was denied
- .deniedBy - Who denied it
- .deniedByEmail - The person's email who denied it
- .ssoValidate - MFA SSO Validated
- .requestTime - Time it was requested locally
- .requestTimeUTC - Time it was requested UTC
- .startTime - Time when the administrative task started locally
- .startTimeUTC - Time when the administrative task started UTC
- .endTime - Time when the administrative task ended locally
- .endTimeUTC - Time when the administrative task ended UTC
- .responseTime - Time it took to responed to the request
- .auditlogLink - The URL to the Auditlog request
