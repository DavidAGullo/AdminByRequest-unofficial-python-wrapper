# AdminByRequest (Unofficial Python Package)

Feel free to use this for your projects if you are developing things with the Admin by Request API. I mostly use this to show proof of concepts of all that is available with the API. This project is still a work in progress so sorry if everything isn't available yet. This is not associated with the Admin by Request company and contains nothing special outside of the already available Public API documented at [Public API &gt;  API Overview](https://www.adminbyrequest.com/en/docs/api-overview)

## Outline

## Functions

### Auditlog API:

This targets all the Auditlog API which includes 5 GET resources:

1. /auditlog - Returns an array of auditlog entries
2. /auditlog/[id] - Returns one auditlog entry by its ID
3. /computers/[computername]/auditlog - Returns an array of auditlog entries for a certain computer
4. /users/[user]/auditlog - Returns an array of auditlog entries for a certain user (user account of full name)
5. /auditlog/delta - Currently this only returns the timeNow value

##### Use / Methods

###### **Get all the Auditlogs** - This just returns all available auditlogs

```python
# The function
def get_auditlog(self):
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


###### **Get the auditlog by it's Identiifier** - Returns one Auditlog

```python
def get_auditlog_id(id=95423844):
	returns auditlog_id

# Returns only the example from the Get all Auditlogs method
```
