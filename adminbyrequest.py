import requests
from enum import Enum
import datetime

class ABRRequestAuditlogObject:
    def __init__(
        self,
        installs,
        uninstalls,
        elevatedApplications,
        scanResults,
        id: int,
        traceNo='',
        settingsName='', 
        runType='', 
        typeCode: int=0, 
        status='', 
        statusCode: int=0, 
        application_file='',
        application_path='',
        application_name='',
        application_vendor='',
        application_version='',
        application_sha256='',
        application_scanResult='',
        application_scanResultCode: int=0,
        application_threat='',
        application_virustotalLink='',
        application_preapproved='',
        user_account='',
        user_fullname='',
        user_email='',
        user_phone='',
        user_isAdmin='',
        computer_name='',
        computer_platform='',
        computer_platformCode: int=0,
        computer_make='',
        computer_model='',
        reason='',
        approvedBy='',
        approvedByEmail='',
        deniedReason='',
        deniedBy='',
        deniedByEmail='',
        ssoValidate='',
        requestTime='',
        requestTimeUTC='',
        startTime='',
        startTimeUTC='',
        endTime='',
        endTimeUTC='',
        responseTime='',
        auditlogLink='',):
        self.installs = installs
        self.uninstalls = uninstalls
        self.elevatedApplications = elevatedApplications
        self.scanResults = scanResults
        self.id = id
        self.traceNo = traceNo
        self.settingsName = settingsName
        self.runType = runType
        self.typeCode = typeCode
        self.status = status
        self.statusCode = statusCode
        self.application_file = application_file
        self.application_path = application_path
        self.application_name = application_name
        self.application_vendor = application_vendor
        self.application_version = application_version
        self.application_sha256 = application_sha256
        self.application_scanResult = application_scanResult
        self.application_scanResultCode = application_scanResultCode
        self.application_threat = application_threat
        self.application_virustotalLink = application_virustotalLink
        self.application_preapproved = application_preapproved
        self.user_account = user_account
        self.user_fullname = user_fullname
        self.user_email = user_email
        self.user_phone = user_phone
        self.user_isAdmin = user_isAdmin
        self.computer_name = computer_name
        self.computer_platform = computer_platform
        self.computer_platformCode = computer_platformCode
        self.computer_make = computer_make
        self.computer_model = computer_model
        self.reason = reason
        self.approvedBy = approvedBy
        self.approvedByEmail = approvedByEmail
        self.deniedReason = deniedReason
        self.deniedBy = deniedBy
        self.deniedByEmail = deniedByEmail
        self.ssoValidate = ssoValidate
        self.requestTime = requestTime
        self.requestTimeUTC = requestTimeUTC
        self.startTime = startTime
        self.startTimeUTC = startTimeUTC
        self.endTime = endTime
        self.endTimeUTC = endTimeUTC
        self.responseTime = responseTime
        self.auditlogLink = auditlogLink
        
class ABRRequestInventoryObject:
    def __init__(
        self, 
        id: int, 
        name, 
        inventoryAvailable, 
        inventoryDate='', 
        clientVersion='', 
        clientInstall='', 
        notes='', 
        user_account='',
        user_fullname='',
        user_email='',
        user_phone='',
        user_isAdmin='',
        user_domain='',
        user_isdomainjoined='',
        user_isAzureJoined='',
        user_orgUnit='',
        user_orgUnitPath='',
        user_groups='',
        owner_account='',
        owner_fullname='',
        computer_domain='',
        computer_domainjoined='',
        computer_isAzureJoined='',
        computer_orgUnit='',
        computer_orgUnitPath='',
        computer_groups='',
        computer_localAdmins='',
        computer_users='',
        os_platform='',
        os_platformCode: int=0,
        os_name='',
        os_version='',
        os_release: int=0,
        os_build: int=0,
        os_buldUpdate: int=0,
        os_type='',
        os_typeCode: int=0,
        os_bits: int=0,
        os_installDate='',
        hardware_make='',
        hardware_model='',
        hardware_type='',
        hardware_typeCode: int=0,
        hardware_serviceTag='',
        hardware_CPU='',
        hardware_CPUspeed: int=0,
        hardware_CPUcores: int=0,
        hardware_diskSize: int=0,
        hardware_diskFree: int=0,
        hardware_diskStatus='',
        hardware_memory: int=0,
        hardware_noMonitors: int=0,
        hardware_monitorResolution='',
        hardware_bitlockerStatus='',
        hardware_isCompliant='',
        hardware_tpmEnabled='',
        hardware_tpmVersion='',
        network_publicIP='',
        network_privateIP='',
        network_mac='',
        hetwork_nicSpeed='',
        network_hostname='',
        location_city='',
        location_region='', #also State
        location_country='',
        location_latitude='',
        location_longitude='',
        googleMaps='',
        hourOffset='',
        software=''):
        self.id = id
        self.name = name
        self.inventoryAvailable = inventoryAvailable
        self.inventoryDate = inventoryDate
        self.clientVersion = clientVersion
        self.clientInstall = clientInstall
        self.notes = notes
        self.user_account = user_account
        self.user_fullname = user_fullname
        self.user_email = user_email
        self.user_phone = user_phone
        self.user_isAdmin = user_isAdmin
        self.user_domain = user_domain
        self.user_isdomainjoined = user_isdomainjoined
        self.user_isAzureJoined = user_isAzureJoined
        self.user_orgUnit = user_orgUnit
        self.user_orgUnitPath = user_orgUnitPath
        self.user_groups = user_groups
        self.owner_account = owner_account
        self.owner_fullname = owner_fullname
        self.computer_domain = computer_domain
        self.computer_domainjoined = computer_domainjoined
        self.computer_isAzureJoined = computer_isAzureJoined
        self.computer_orgUnit = computer_orgUnit
        self.computer_orgUnitPath = computer_orgUnitPath
        self.computer_groups = computer_groups
        self.computer_localAdmins = computer_localAdmins
        self.computer_users = computer_users
        self.os_platform = os_platform
        self.os_platformCode = os_platformCode
        self.os_name = os_name
        self.os_version = os_version
        self.os_release = os_release
        self.os_build = os_build
        self.os_buldUpdate = os_buldUpdate
        self.os_type = os_type
        self.os_typeCode = os_typeCode
        self.os_bits = os_bits
        self.os_installDate = os_installDate
        self.hardware_make = hardware_make
        self.hardware_model = hardware_model
        self.hardware_type = hardware_type
        self.hardware_typeCode = hardware_typeCode
        self.hardware_serviceTag = hardware_serviceTag
        self.hardware_CPU = hardware_CPU
        self.hardware_CPUspeed = hardware_CPUspeed
        self.hardware_CPUcores = hardware_CPUcores
        self.hardware_diskSize = hardware_diskSize
        self.hardware_diskFree = hardware_diskFree
        self.hardware_diskStatus = hardware_diskStatus
        self.hardware_memory = hardware_memory
        self.hardware_noMonitors = hardware_noMonitors
        self.hardware_monitorResolution = hardware_monitorResolution
        self.hardware_bitlockerStatus = hardware_bitlockerStatus
        self.hardware_isCompliant = hardware_isCompliant
        self.hardware_tpmEnabled = hardware_tpmEnabled
        self.hardware_tpmVersion = hardware_tpmVersion
        self.network_publicIP = network_publicIP
        self.network_privateIP = network_privateIP
        self.network_mac = network_mac
        self.hetwork_nicSpeed = hetwork_nicSpeed
        self.network_hostname = network_hostname
        self.location_city = location_city
        self.location_region = location_region
        self.location_country = location_country
        self.location_latitude = location_latitude
        self.location_longitude = location_longitude
        self.googleMaps = googleMaps
        self.hourOffset = hourOffset
        self.software = software
        
class ABRRequestRequestsObject:
    def __init__(
        self,
        scanResults = None,
        id: int=0,
        traceNo = '',
        settingsName = '',
        runType = '',
        typeCode: int = 0,
        status = '',
        statusCode: int = 0,
        application_file = '',
        application_name = '',
        application_vendor = '',
        application_version = '',
        application_sha256 = '',
        application_scanResult = '',
        application_scanResultCode: int = 0,
        application_threat = '',
        application_virustotalLink = '',
        user_account = '',
        user_fullname = '',
        user_email = '',
        user_phone = '',
        computer_name = '',
        computer_platform = '',
        computer_platformCode: int = 0,
        computer_make = '',
        computer_model = '',
        reason = '',
        approvedBy = '',
        approvedByEmail = '',
        deniedReason = '',
        deniedBy = '',
        deniedByEmail = '',
        requestTime = '',
        auditlogLink = ''):
        self.scanResults = scanResults
        self.id = id
        self.traceNo = traceNo
        self.settingsName = settingsName
        self.runType = runType
        self.typeCode = typeCode
        self.status = status
        self.statusCode = statusCode
        self.application_file = application_file
        self.application_name = application_name
        self.application_vendor = application_vendor
        self.application_version = application_version
        self.application_sha256 = application_sha256
        self.application_scanResult = application_scanResult
        self.application_scanResultCode = application_scanResultCode
        self.application_threat = application_threat
        self.application_virustotalLink = application_virustotalLink
        self.user_account = user_account
        self.user_fullname = user_fullname
        self.user_email = user_email
        self.user_phone = user_phone
        self.computer_name = computer_name
        self.computer_platform = computer_platform
        self.computer_platformCode = computer_platformCode
        self.computer_make = computer_make
        self.computer_model = computer_model
        self.reason = reason
        self.approvedBy = approvedBy
        self.approvedByEmail = approvedByEmail
        self.deniedReason = deniedReason
        self.deniedBy = deniedBy
        self.deniedByEmail = deniedByEmail
        self.requestTime = requestTime
        self.auditlogLink = auditlogLink
        
class ABRRequestEventObjects:
    def __init__(
        self,
        id: int=0,
        eventCode: int=0,
        eventLevel: int=0,
        eventText='',
        eventTime='',
        eventTimeUTC='',
        computerName='',
        userAccount='',
        userName='',
        alertAccount='',
        auditLogURL='',
        rollback='',
        additionalData='',
        application_file='',
        application_path='',
        application_name='',
        application_vendor='',
        application_version='',
        application_sha256=''):
        self.id = id
        self.eventCode = eventCode
        self.eventLevel = eventLevel
        self.eventText = eventText
        self.eventTime = eventTime
        self.eventTimeUTC = eventTimeUTC
        self.computerName = computerName
        self.userAccount = userAccount
        self.userName = userName
        self.alertAccount = alertAccount
        self.auditLogURL = auditLogURL
        self.rollback = rollback
        self.additionalData = additionalData
        self.application_file = application_file
        self.application_path = application_path
        self.application_name = application_name
        self.application_vendor = application_vendor
        self.application_version = application_version
        self.application_sha256 = application_sha256
           
class ABREventCodes(Enum):
    User_Added_Admin = 1
    User_Removed_Admin = 2
    Group_Removed_Admin = 3
    Audited_Admin_Login = 5
    UnAudited_Admin_Login = 6
    Support_Assist_Initiated = 8
    Password_Changed = 10
    LocalUser_Disabled = 11
    LocalUser_Enabled = 12
    LocalUser_Created = 13
    LocalUser_Deleted = 14
    PolicyRegistry_Changed = 20
    PolicyRegistry_Added = 21
    Uninstall_Attempted = 30
    Uninstall_byPin = 31
    Uninstall_Pin_Failed = 32
    ABR_Installed = 40
    ABR_Uninstalled = 41
    ABR_Server_Installed = 42
    ABR_Server_Uninstalled = 43
    ABR_Diagnostics_Sent = 50
    User_ResturedAdmin = 60
    Group_RestoredAdmin = 61
    Breakglass_Created = 70
    Breakglass_Removed = 71
    Breakglass_Login = 72
    Breakglass_ClockTampering = 73
    Azure_DeviceAdmin_Restored = 80
    Azure_CompanyAdmin_Restored = 81
    AdminSession_Denied = 90
    AdminSession_ClockTampering = 91
    ExecutionBlocked_Policy = 92
    ExecutionBlocked_Malware = 93
    ExecutionBlocked_LikeyMalware = 94
    AdminSession_Pin_Used = 95
    ApplicationBlocked_Pin_Used = 97
    ElevatedApplication_Pin_Used = 98
    ApplicationBlocked_Pin2_Issued = 100
    Uninstall_Pin_Issued = 101
    Breakglass_Account_Issued = 102
    AdminSession_Pin2_Issued = 103
    LocalAdmin_Account_Revoked = 110
    LocalAdmin_Group_Revoked = 111
    LocalAdmin_Account_CancelRevoke = 112
    LocalAdmin_Group_CancelRevoke = 113
    LocalAdmin_Account_Restored = 114
    LocalAdmin_Group_Restored = 115
    LocalAdmin_Account_CancelRestore = 116
    LocalAdmin_Group_CancelRestore = 117
    DeviceOwner_Set = 120
    DeviceOwner_Released = 121
    DeviceOwner_Set_Admin = 122
    AdminSession_Denied_NotOwner = 123
    ExecutionBlocked_NotOwner = 124
    AdminSession_Denied_NotIntuneCompliant = 130
    ExecutionBlocked_NotIntuneCompliant = 131
    RemoteDesktop_Account_Revoke = 140
    RemoteDesktop_Group_Revoke = 141
    RemoteDesktop_Account_CancelRevoke = 142
    RemoteDesktop_Group_CancelRevoke = 143
    RemoteDesktop_Account_Restore = 144
    RemoteDesktop_Group_Restore = 145
    RemoteDesktop_Account_CancelRestore = 146
    RemoteDesktop_Group_CancelRestore = 147
    User_Removed_RemoteDesktop = 150
    Group_Removed_RemoteDesktop = 151
    User_Restored_RemoteDesktop = 152
    Group_Restored_RemoteDesktop = 153
    LocalAdmin_Account_AdditionIssued = 160
    LocalAdmin_Group_AdditionIssued = 161
    LocalAdmin_Account_AdditionCancelled = 162
    LocalAdmin_Group_AdditionCancelled = 163
    RemoteDesktop_Account_AdditionIssued = 170
    RemoteDesktop_Group_AdditionIssued = 171
    RemoteDesktop_Account_AdditionCancelled = 172
    RemoteDesktop_Group_AdditionCancelled = 173
    RotatingAdmin_Account_Created = 180
    RotatingAdmin_Account_Removed = 181
    RotatingAdmin_Account_Login = 182
     
class ABRDatacenter(Enum):
    dc1 = 'dc1'
    dc2 = 'dc2'
    
class AdminByRequest:  
    def __init__(self, apikey, datacenter=ABRDatacenter.dc1):
        self.datacenter = datacenter
        self.api_key = apikey
        self.url = ''
        if datacenter == ABRDatacenter.dc1:
            self.url = 'https://dc1api.adminbyrequest.com/'
        elif datacenter == ABRDatacenter.dc2:
            self.url = 'https://dc2api.adminbyrequest.com/'
            
        
# /auditlog - Audit Log API extension

    # Get all audit logs as JSON
    def get_auditlog(self, limit:int = 10000, offset: int=0):
        url=''
        if offset > 0:
            url = self.url + 'auditlog?limit=' + str(limit) + '&offset=' + str(offset)
        elif offset == 0:
            url = self.url + 'auditlog?limit=' + str(limit)
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        auditlog = response.json()
        audit_obj = {}
        count = 0
        
        # Error Checking debugging issue with Users seeing issues when using the wrong Datacenter
        try:
            for item in auditlog:
                audit_obj[count] = ABRRequestAuditlogObject( 
                    installs=item['installs'],
                    uninstalls=item['uninstalls'],
                    elevatedApplications=item['elevatedApplications'],
                    scanResults=item['scanResults'],
                    id=item['id'],
                    traceNo=item['traceNo'],
                    settingsName=item['settingsName'],
                    runType=item['type'],
                    typeCode=item['typeCode'],
                    status=item['status'],
                    statusCode=item['statusCode'],
                    application_file=item['application']['file'],
                    application_path=item['application']['path'],
                    application_name=item['application']['name'],
                    application_vendor=item['application']['vendor'],
                    application_version=item['application']['version'],
                    application_sha256=item['application']['sha256'],
                    application_scanResult=item['application']['scanResult'],
                    application_scanResultCode=item['application']['scanResultCode'],
                    application_threat=item['application']['threat'],
                    application_virustotalLink=item['application']['virustotalLink'],
                    application_preapproved=item['application']['preapproved'],
                    user_account=item['user']['account'],
                    user_fullname=item['user']['fullName'],
                    user_email=item['user']['email'],
                    user_phone=item['user']['phone'],
                    user_isAdmin=item['user']['isAdmin'],
                    computer_name=item['computer']['name'],
                    computer_platform=item['computer']['platform'],
                    computer_platformCode=item['computer']['platformCode'],
                    computer_make=item['computer']['make'],
                    computer_model=item['computer']['model'],
                    reason=item['reason'],
                    approvedBy=item['approvedBy'],
                    approvedByEmail=item['approvedByEmail'],
                    deniedReason=item['deniedReason'],
                    deniedBy=item['deniedBy'],
                    deniedByEmail=item['deniedByEmail'],
                    ssoValidate=item['ssoValidated'],
                    requestTime=item['requestTime'],
                    requestTimeUTC=item['requestTimeUTC'],
                    startTime=item['startTime'],
                    startTimeUTC=item['startTimeUTC'],
                    endTime=item['endTime'],
                    endTimeUTC=item['endTimeUTC'],
                    responseTime=item['responseTime'],
                    auditlogLink=item['auditlogLink']
                )
                count += 1
            return audit_obj
        except Exception as e:
            print("Error: " + str(e))
            if auditlog['Message'] == 'Invalid API key':
                print("Message: " + auditlog['Message'] + " Check your API Key/Datacenter DC1 is EU and DC2 is US")
    
    # Get audit log by ID as JSON
    def get_auditlog_id(self, id: int):
        url = self.url + 'auditlog/' + str(id)
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        auditlog = response.json()
        try:
            audit_obj = ABRRequestAuditlogObject( 
                installs=auditlog['installs'],
                uninstalls=auditlog['uninstalls'],
                elevatedApplications=auditlog['elevatedApplications'],
                scanResults=auditlog['scanResults'],
                id=auditlog['id'],
                traceNo=auditlog['traceNo'],
                settingsName=auditlog['settingsName'],
                runType=auditlog['type'],
                typeCode=auditlog['typeCode'],
                status=auditlog['status'],
                statusCode=auditlog['statusCode'],
                application_file=auditlog['application']['file'],
                application_path=auditlog['application']['path'],
                application_name=auditlog['application']['name'],
                application_vendor=auditlog['application']['vendor'],
                application_version=auditlog['application']['version'],
                application_sha256=auditlog['application']['sha256'],
                application_scanResult=auditlog['application']['scanResult'],
                application_scanResultCode=auditlog['application']['scanResultCode'],
                application_threat=auditlog['application']['threat'],
                application_virustotalLink=auditlog['application']['virustotalLink'],
                application_preapproved=auditlog['application']['preapproved'],
                user_account=auditlog['user']['account'],
                user_fullname=auditlog['user']['fullName'],
                user_email=auditlog['user']['email'],
                user_phone=auditlog['user']['phone'],
                user_isAdmin=auditlog['user']['isAdmin'],
                computer_name=auditlog['computer']['name'],
                computer_platform=auditlog['computer']['platform'],
                computer_platformCode=auditlog['computer']['platformCode'],
                computer_make=auditlog['computer']['make'],
                computer_model=auditlog['computer']['model'],
                reason=auditlog['reason'],
                approvedBy=auditlog['approvedBy'],
                approvedByEmail=auditlog['approvedByEmail'],
                deniedReason=auditlog['deniedReason'],
                deniedBy=auditlog['deniedBy'],
                deniedByEmail=auditlog['deniedByEmail'],
                ssoValidate=auditlog['ssoValidated'],
                requestTime=auditlog['requestTime'],
                requestTimeUTC=auditlog['requestTimeUTC'],
                startTime=auditlog['startTime'],
                startTimeUTC=auditlog['startTimeUTC'],
                endTime=auditlog['endTime'],
                endTimeUTC=auditlog['endTimeUTC'],
                responseTime=auditlog['responseTime'],
                auditlogLink=auditlog['auditlogLink']
            )
            return audit_obj
        except Exception as e:
            print("Error: " + str(e))
            if auditlog['Message'] == 'Invalid API key':
                print("Message: " + auditlog['Message'] + " Check your API Key/Datacenter DC1 is EU and DC2 is US")
    
    # Get audit log by computer as JSON
    def get_auditlog_computer(self, computername: str):
        url = self.url + 'computers/' + computername + "/auditlog"
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        auditlog = response.json()
        audit_obj = {}
        count = 0
        try:
            for item in auditlog:
                audit_obj[count] = ABRRequestAuditlogObject( 
                    installs=item['installs'],
                    uninstalls=item['uninstalls'],
                    elevatedApplications=item['elevatedApplications'],
                    scanResults=item['scanResults'],
                    id=item['id'],
                    traceNo=item['traceNo'],
                    settingsName=item['settingsName'],
                    runType=item['type'],
                    typeCode=item['typeCode'],
                    status=item['status'],
                    statusCode=item['statusCode'],
                    application_file=item['application']['file'],
                    application_path=item['application']['path'],
                    application_name=item['application']['name'],
                    application_vendor=item['application']['vendor'],
                    application_version=item['application']['version'],
                    application_sha256=item['application']['sha256'],
                    application_scanResult=item['application']['scanResult'],
                    application_scanResultCode=item['application']['scanResultCode'],
                    application_threat=item['application']['threat'],
                    application_virustotalLink=item['application']['virustotalLink'],
                    application_preapproved=item['application']['preapproved'],
                    user_account=item['user']['account'],
                    user_fullname=item['user']['fullName'],
                    user_email=item['user']['email'],
                    user_phone=item['user']['phone'],
                    user_isAdmin=item['user']['isAdmin'],
                    computer_name=item['computer']['name'],
                    computer_platform=item['computer']['platform'],
                    computer_platformCode=item['computer']['platformCode'],
                    computer_make=item['computer']['make'],
                    computer_model=item['computer']['model'],
                    reason=item['reason'],
                    approvedBy=item['approvedBy'],
                    approvedByEmail=item['approvedByEmail'],
                    deniedReason=item['deniedReason'],
                    deniedBy=item['deniedBy'],
                    deniedByEmail=item['deniedByEmail'],
                    ssoValidate=item['ssoValidated'],
                    requestTime=item['requestTime'],
                    requestTimeUTC=item['requestTimeUTC'],
                    startTime=item['startTime'],
                    startTimeUTC=item['startTimeUTC'],
                    endTime=item['endTime'],
                    endTimeUTC=item['endTimeUTC'],
                    responseTime=item['responseTime'],
                    auditlogLink=item['auditlogLink']
                )
                count += 1
            return audit_obj
        except Exception as e:
            print("Error: " + str(e))
            if auditlog['Message'] == 'Invalid API key':
                print("Message: " + auditlog['Message'] + " Check your API Key/Datacenter DC1 is EU and DC2 is US")
    
    # Get audit log by user as JSON
    def get_auditlog_username(self, username: str):
        url = self.url + 'users/' + username + "/auditlog"
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        auditlog = response.json()
        audit_obj = {}
        count = 0
        
        try:
            for item in auditlog:
                audit_obj[count] = ABRRequestAuditlogObject( 
                    installs=item['installs'],
                    uninstalls=item['uninstalls'],
                    elevatedApplications=item['elevatedApplications'],
                    scanResults=item['scanResults'],
                    id=item['id'],
                    traceNo=item['traceNo'],
                    settingsName=item['settingsName'],
                    runType=item['type'],
                    typeCode=item['typeCode'],
                    status=item['status'],
                    statusCode=item['statusCode'],
                    application_file=item['application']['file'],
                    application_path=item['application']['path'],
                    application_name=item['application']['name'],
                    application_vendor=item['application']['vendor'],
                    application_version=item['application']['version'],
                    application_sha256=item['application']['sha256'],
                    application_scanResult=item['application']['scanResult'],
                    application_scanResultCode=item['application']['scanResultCode'],
                    application_threat=item['application']['threat'],
                    application_virustotalLink=item['application']['virustotalLink'],
                    application_preapproved=item['application']['preapproved'],
                    user_account=item['user']['account'],
                    user_fullname=item['user']['fullName'],
                    user_email=item['user']['email'],
                    user_phone=item['user']['phone'],
                    user_isAdmin=item['user']['isAdmin'],
                    computer_name=item['computer']['name'],
                    computer_platform=item['computer']['platform'],
                    computer_platformCode=item['computer']['platformCode'],
                    computer_make=item['computer']['make'],
                    computer_model=item['computer']['model'],
                    reason=item['reason'],
                    approvedBy=item['approvedBy'],
                    approvedByEmail=item['approvedByEmail'],
                    deniedReason=item['deniedReason'],
                    deniedBy=item['deniedBy'],
                    deniedByEmail=item['deniedByEmail'],
                    ssoValidate=item['ssoValidated'],
                    requestTime=item['requestTime'],
                    requestTimeUTC=item['requestTimeUTC'],
                    startTime=item['startTime'],
                    startTimeUTC=item['startTimeUTC'],
                    endTime=item['endTime'],
                    endTimeUTC=item['endTimeUTC'],
                    responseTime=item['responseTime'],
                    auditlogLink=item['auditlogLink']
                )
                count += 1
            return audit_obj
        except Exception as e:
            print("Error: " + str(e))
            if auditlog['Message'] == 'Invalid API key':
                print("Message: " + auditlog['Message'] + " Check your API Key/Datacenter DC1 is EU and DC2 is US")
    
    # Get the timeNow Value which will be used to calculate until the next delta [This number increases by second]
    def get_auditlogs_delta(self, fullLog: bool=False):
        url = self.url + 'auditlog/delta?limit=10000'
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        if fullLog:
            return data
        elif not fullLog:
            time = data['timeNow']
        return time

# /inventory - Inventory API extension
    # Get all inventory items as JSON
    def get_inventory(self, limit: int=10000, offset: int=0):
        url=''
        if offset > 0:
            url = self.url + 'inventory?limit=' + str(limit) + '&offset=' + str(offset)
        elif offset == 0:
            url = self.url + 'inventory?limit=' + str(limit)
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        inventory = response.json()
        inv_obj = {}
        count = 0
        
        # Error Checking debugging issue with Users seeing issues when using the wrong Datacenter
        try:
            for item in inventory:
                if item['inventoryAvailable']:
                    inv_obj[count] = ABRRequestInventoryObject(
                        item['id'],
                        item["name"],
                        item['inventoryAvailable'],
                        item['inventoryDate'],
                        item['abrClientVersion'],
                        item['abrClientInstallDate'],
                        item['notes'],
                        item['user']['account'],
                        item['user']['fullName'],
                        item['user']['email'],
                        item['user']['phone'],
                        item['user']['isAdmin'],
                        item['user']['domain'],
                        item['user']['isDomainJoined'],
                        item['user']['isAzureJoined'],
                        item['user']['orgUnit'],
                        item['user']['orgUnitPath'],
                        item['user']['groups'],
                        item['owner']['account'],
                        item['owner']['fullName'],
                        item['computer']['domain'],
                        item['computer']['isDomainJoined'],
                        item['computer']['isAzureJoined'],
                        item['computer']['orgUnit'],
                        item['computer']['orgUnitPath'],
                        item['computer']['groups'],
                        item['computer']['localAdmins'],
                        item['computer']['users'],
                        item['operatingSystem']['platform'],
                        item['operatingSystem']['platformCode'],
                        item['operatingSystem']['name'],
                        item['operatingSystem']['version'],
                        item['operatingSystem']['release'],
                        item['operatingSystem']['build'],
                        item['operatingSystem']['buildUpdate'],
                        item['operatingSystem']['type'],
                        item['operatingSystem']['typeCode'],
                        item['operatingSystem']['bits'],
                        item['operatingSystem']['installDate'],
                        item['hardware']['make'],
                        item['hardware']['model'],
                        item['hardware']['type'],
                        item['hardware']['typeCode'],
                        item['hardware']['serviceTag'],
                        item['hardware']['cpu'],
                        item['hardware']['cpuSpeed'],
                        item['hardware']['cpuCores'],
                        item['hardware']['diskSize'],
                        item['hardware']['diskFree'],
                        item['hardware']['diskStatus'],
                        item['hardware']['memory'],
                        item['hardware']['noMonitors'],
                        item['hardware']['monitorResolution'],
                        item['hardware']['bitlockerEnabled'],
                        item['hardware']['isCompliant'],
                        item['hardware']['tpmEnabled'],
                        item['hardware']['tpmVersion'],
                        item['network']['publicIP'],
                        item['network']['privateIP'],
                        item['network']['macAddress'],
                        item['network']['nicSpeed'],
                        item['network']['hostName'],
                        item['location']['city'],
                        item['location']['region'],
                        item['location']['country'],
                        item['location']['latitude'],
                        item['location']['longitude'],
                        item['location']['googleMapsLink'],
                        item['location']['hourOffset'],
                        item['software']
                    )
                    count += 1
            return inv_obj
        except Exception as e:
            print("Error: " + str(e))
            if inventory['Message'] == 'Invalid API key':
                print("Message: " + inventory['Message'] + "Check your API Key/Datacenter DC1 is EU and DC2 is US")
    
    # Get inventory item by ID as JSON
    def get_inventory_id(self, id: int):
        url = self.url + 'inventory/' + str(id)
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        inventory = response.json()
        
        try:
            inv_obj= ABRRequestInventoryObject(
                inventory['id'],
                inventory["name"],
                inventory['inventoryAvailable'],
                inventory['inventoryDate'],
                inventory['abrClientVersion'],
                inventory['abrClientInstallDate'],
                inventory['notes'],
                inventory['user']['account'],
                inventory['user']['fullName'],
                inventory['user']['email'],
                inventory['user']['phone'],
                inventory['user']['isAdmin'],
                inventory['user']['domain'],
                inventory['user']['isDomainJoined'],
                inventory['user']['isAzureJoined'],
                inventory['user']['orgUnit'],
                inventory['user']['orgUnitPath'],
                inventory['user']['groups'],
                inventory['owner']['account'],
                inventory['owner']['fullName'],
                inventory['computer']['domain'],
                inventory['computer']['isDomainJoined'],
                inventory['computer']['isAzureJoined'],
                inventory['computer']['orgUnit'],
                inventory['computer']['orgUnitPath'],
                inventory['computer']['groups'],
                inventory['computer']['localAdmins'],
                inventory['computer']['users'],
                inventory['operatingSystem']['platform'],
                inventory['operatingSystem']['platformCode'],
                inventory['operatingSystem']['name'],
                inventory['operatingSystem']['version'],
                inventory['operatingSystem']['release'],
                inventory['operatingSystem']['build'],
                inventory['operatingSystem']['buildUpdate'],
                inventory['operatingSystem']['type'],
                inventory['operatingSystem']['typeCode'],
                inventory['operatingSystem']['bits'],
                inventory['operatingSystem']['installDate'],
                inventory['hardware']['make'],
                inventory['hardware']['model'],
                inventory['hardware']['type'],
                inventory['hardware']['typeCode'],
                inventory['hardware']['serviceTag'],
                inventory['hardware']['cpu'],
                inventory['hardware']['cpuSpeed'],
                inventory['hardware']['cpuCores'],
                inventory['hardware']['diskSize'],
                inventory['hardware']['diskFree'],
                inventory['hardware']['diskStatus'],
                inventory['hardware']['memory'],
                inventory['hardware']['noMonitors'],
                inventory['hardware']['monitorResolution'],
                inventory['hardware']['bitlockerEnabled'],
                inventory['hardware']['isCompliant'],
                inventory['hardware']['tpmEnabled'],
                inventory['hardware']['tpmVersion'],
                inventory['network']['publicIP'],
                inventory['network']['privateIP'],
                inventory['network']['macAddress'],
                inventory['network']['nicSpeed'],
                inventory['network']['hostName'],
                inventory['location']['city'],
                inventory['location']['region'],
                inventory['location']['country'],
                inventory['location']['latitude'],
                inventory['location']['longitude'],
                inventory['location']['googleMapsLink'],
                inventory['location']['hourOffset'],
                inventory['software']
            )
            return inv_obj
        except Exception as e:
            print("Error: " + str(e))
            if inventory['Message'] == 'Invalid API key':
                print("Message: " + inventory['Message'] + "Check your API Key/Datacenter DC1 is EU and DC2 is US")
        
    # Get inventory item by computer as JSON
    def get_inventory_computer(self, computername: str):
        url = self.url + "/inventory/" + computername
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        inventory = response.json()
        
        try:
            inv_obj= ABRRequestInventoryObject(
                inventory['id'],
                inventory['name'],
                inventory['inventoryAvailable'],
                inventory['inventoryDate'],
                inventory['abrClientVersion'],
                inventory['abrClientInstallDate'],
                inventory['notes'],
                inventory['user']['account'],
                inventory['user']['fullName'],
                inventory['user']['email'],
                inventory['user']['phone'],
                inventory['user']['isAdmin'],
                inventory['user']['domain'],
                inventory['user']['isDomainJoined'],
                inventory['user']['isAzureJoined'],
                inventory['user']['orgUnit'],
                inventory['user']['orgUnitPath'],
                inventory['user']['groups'],
                inventory['owner']['account'],
                inventory['owner']['fullName'],
                inventory['computer']['domain'],
                inventory['computer']['isDomainJoined'],
                inventory['computer']['isAzureJoined'],
                inventory['computer']['orgUnit'],
                inventory['computer']['orgUnitPath'],
                inventory['computer']['groups'],
                inventory['computer']['localAdmins'],
                inventory['computer']['users'],
                inventory['operatingSystem']['platform'],
                inventory['operatingSystem']['platformCode'],
                inventory['operatingSystem']['name'],
                inventory['operatingSystem']['version'],
                inventory['operatingSystem']['release'],
                inventory['operatingSystem']['build'],
                inventory['operatingSystem']['buildUpdate'],
                inventory['operatingSystem']['type'],
                inventory['operatingSystem']['typeCode'],
                inventory['operatingSystem']['bits'],
                inventory['operatingSystem']['installDate'],
                inventory['hardware']['make'],
                inventory['hardware']['model'],
                inventory['hardware']['type'],
                inventory['hardware']['typeCode'],
                inventory['hardware']['serviceTag'],
                inventory['hardware']['cpu'],
                inventory['hardware']['cpuSpeed'],
                inventory['hardware']['cpuCores'],
                inventory['hardware']['diskSize'],
                inventory['hardware']['diskFree'],
                inventory['hardware']['diskStatus'],
                inventory['hardware']['memory'],
                inventory['hardware']['noMonitors'],
                inventory['hardware']['monitorResolution'],
                inventory['hardware']['bitlockerEnabled'],
                inventory['hardware']['isCompliant'],
                inventory['hardware']['tpmEnabled'],
                inventory['hardware']['tpmVersion'],
                inventory['network']['publicIP'],
                inventory['network']['privateIP'],
                inventory['network']['macAddress'],
                inventory['network']['nicSpeed'],
                inventory['network']['hostName'],
                inventory['location']['city'],
                inventory['location']['region'],
                inventory['location']['country'],
                inventory['location']['latitude'],
                inventory['location']['longitude'],
                inventory['location']['googleMapsLink'],
                inventory['location']['hourOffset'],
                inventory['software']
            )
            return inv_obj
        except Exception as e:
            print("Error: " + str(e))
            if inventory['Message'] == 'Invalid API key':
                print("Message: " + inventory['Message'] + "Check your API Key/Datacenter DC1 is EU and DC2 is US")
        
    # Delete Inventory by ID
    def delete_inventory_id(self, id: int):
        url = self.url + 'inventory/' + str(id)
        headers = {
            "apikey": self.api_key
        }
        requests.delete(url, headers=headers)
        
    # Delete Inventory by computer
    def delete_inventory_computer(self, computername: str):
        url = self.url + 'inventory/' + computername
        headers = {
            "apikey": self.api_key
        }
        requests.delete(url, headers=headers)
        

    # Functional Functions
    # Get Computers where InventoryDate is older than X days
    def get_inventory_by_date(self, days: int, limit: int=10000, unavailable=False):
        # Convert days to "YYYY-MM-DD T HH:MM:SS.MlS" format
        days = datetime.datetime.now() - datetime.timedelta(days=days)
        days = days.strftime('%Y-%m-%dT%H:%M:%S.%f')[:- 3]

        url = self.url + 'inventory?limit=' + str(limit)
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        inventory = response.json()
        inv_obj = {}
        count = 0
        
        try:
            # Filter inventory items by availability and date in a single pass
            if unavailable:
                for item in inventory:
                    if not item['inventoryAvailable'] or (item['inventoryAvailable'] and item['inventoryDate'] < days):
                        inv_obj[count] = ABRRequestInventoryObject(
                            item['id'],
                            item['name'],
                            item['inventoryAvailable'],
                            item['inventoryDate'],
                            item['abrClientVersion'],
                            item['abrClientInstallDate'],
                            item['notes'],
                            item['user']['account'],
                            item['user']['fullName'],
                            item['user']['email'],
                            item['user']['phone'],
                            item['user']['isAdmin'],
                            item['user']['domain'],
                            item['user']['isDomainJoined'],
                            item['user']['isAzureJoined'],
                            item['user']['orgUnit'],
                            item['user']['orgUnitPath'],
                            item['user']['groups'],
                            item['owner']['account'],
                            item['owner']['fullName'],
                            item['computer']['domain'],
                            item['computer']['isDomainJoined'],
                            item['computer']['isAzureJoined'],
                            item['computer']['orgUnit'],
                            item['computer']['orgUnitPath'],
                            item['computer']['groups'],
                            item['computer']['localAdmins'],
                            item['computer']['users'],
                            item['operatingSystem']['platform'],
                            item['operatingSystem']['platformCode'],
                            item['operatingSystem']['name'],
                            item['operatingSystem']['version'],
                            item['operatingSystem']['release'],
                            item['operatingSystem']['build'],
                            item['operatingSystem']['buildUpdate'],
                            item['operatingSystem']['type'],
                            item['operatingSystem']['typeCode'],
                            item['operatingSystem']['bits'],
                            item['operatingSystem']['installDate'],
                            item['hardware']['make'],
                            item['hardware']['model'],
                            item['hardware']['type'],
                            item['hardware']['typeCode'],
                            item['hardware']['serviceTag'],
                            item['hardware']['cpu'],
                            item['hardware']['cpuSpeed'],
                            item['hardware']['cpuCores'],
                            item['hardware']['diskSize'],
                            item['hardware']['diskFree'],
                            item['hardware']['diskStatus'],
                            item['hardware']['memory'],
                            item['hardware']['noMonitors'],
                            item['hardware']['monitorResolution'],
                            item['hardware']['bitlockerEnabled'],
                            item['hardware']['isCompliant'],
                            item['hardware']['tpmEnabled'],
                            item['hardware']['tpmVersion'],
                            item['network']['publicIP'],
                            item['network']['privateIP'],
                            item['network']['macAddress'],
                            item['network']['nicSpeed'],
                            item['network']['hostName'],
                            item['location']['city'],
                            item['location']['region'],
                            item['location']['country'],
                            item['location']['latitude'],
                            item['location']['longitude'],
                            item['location']['googleMapsLink'],
                            item['location']['hourOffset'],
                            item['software']
                        )
                        count += 1
            else:
                for item in inventory:
                    if item['inventoryAvailable'] and item['inventoryDate'] < days:
                        inv_obj[count] = ABRRequestInventoryObject(
                            item['id'],
                            item['name'],
                            item['inventoryAvailable'],
                            item['inventoryDate'],
                            item['abrClientVersion'],
                            item['abrClientInstallDate'],
                            item['notes'],
                            item['user']['account'],
                            item['user']['fullName'],
                            item['user']['email'],
                            item['user']['phone'],
                            item['user']['isAdmin'],
                            item['user']['domain'],
                            item['user']['isDomainJoined'],
                            item['user']['isAzureJoined'],
                            item['user']['orgUnit'],
                            item['user']['orgUnitPath'],
                            item['user']['groups'],
                            item['owner']['account'],
                            item['owner']['fullName'],
                            item['computer']['domain'],
                            item['computer']['isDomainJoined'],
                            item['computer']['isAzureJoined'],
                            item['computer']['orgUnit'],
                            item['computer']['orgUnitPath'],
                            item['computer']['groups'],
                            item['computer']['localAdmins'],
                            item['computer']['users'],
                            item['operatingSystem']['platform'],
                            item['operatingSystem']['platformCode'],
                            item['operatingSystem']['name'],
                            item['operatingSystem']['version'],
                            item['operatingSystem']['release'],
                            item['operatingSystem']['build'],
                            item['operatingSystem']['buildUpdate'],
                            item['operatingSystem']['type'],
                            item['operatingSystem']['typeCode'],
                            item['operatingSystem']['bits'],
                            item['operatingSystem']['installDate'],
                            item['hardware']['make'],
                            item['hardware']['model'],
                            item['hardware']['type'],
                            item['hardware']['typeCode'],
                            item['hardware']['serviceTag'],
                            item['hardware']['cpu'],
                            item['hardware']['cpuSpeed'],
                            item['hardware']['cpuCores'],
                            item['hardware']['diskSize'],
                            item['hardware']['diskFree'],
                            item['hardware']['diskStatus'],
                            item['hardware']['memory'],
                            item['hardware']['noMonitors'],
                            item['hardware']['monitorResolution'],
                            item['hardware']['bitlockerEnabled'],
                            item['hardware']['isCompliant'],
                            item['hardware']['tpmEnabled'],
                            item['hardware']['tpmVersion'],
                            item['network']['publicIP'],
                            item['network']['privateIP'],
                            item['network']['macAddress'],
                            item['network']['nicSpeed'],
                            item['network']['hostName'],
                            item['location']['city'],
                            item['location']['region'],
                            item['location']['country'],
                            item['location']['latitude'],
                            item['location']['longitude'],
                            item['location']['googleMapsLink'],
                            item['location']['hourOffset'],
                            item['software']
                        )
                        count += 1
            return inv_obj
        except Exception as e:
            print("Error: " + str(e))
            if inventory['Message'] == 'Invalid API key':
                print("Message: " + inventory['Message'] + "Check your API Key/Datacenter DC1 is EU and DC2 is US")
    
# /request - Request API extension
    # Get all requests as JSON
    def get_requests(self, limit: int=10000, offset: int=0):
        url = self.url + 'requests?limit=' + str(limit) + '&offset=' + str(offset)
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        request = response.json()
        request_obj = {}
        count = 0
        # Error Checking debugging issue with Users seeing issues when using the wrong Datacenter
        try:
            for item in request:
                request_obj[count] = ABRRequestRequestsObject(
                    scanResults=item['scanResults'],
                    id=item['id'],
                    traceNo=item['traceNo'],
                    settingsName=item['settingsName'],
                    runType=item['type'],
                    typeCode=item['typeCode'],
                    status=item['status'],
                    statusCode=item['statusCode'],
                    application_file=item['application']['file'],
                    application_name=item['application']['name'],
                    application_vendor=item['application']['vendor'],
                    application_version=item['application']['version'],
                    application_sha256=item['application']['sha256'],
                    application_scanResult=item['application']['scanResult'],
                    application_scanResultCode=item['application']['scanResultCode'],
                    application_threat=item['application']['threat'],
                    application_virustotalLink=item['application']['virustotalLink'],
                    user_account=item['user']['account'],
                    user_fullname=item['user']['fullName'],
                    user_email=item['user']['email'],
                    user_phone=item['user']['phone'],
                    computer_name=item['computer']['name'],
                    computer_platform=item['computer']['platform'],
                    computer_platformCode=item['computer']['platformCode'],
                    computer_make=item['computer']['make'],
                    computer_model=item['computer']['model'],
                    reason=item['reason'],
                    approvedBy=item['approvedBy'],
                    approvedByEmail=item['approvedByEmail'],
                    deniedReason=item['deniedReason'],
                    deniedBy=item['deniedBy'],
                    deniedByEmail=item['deniedByEmail'],
                    requestTime=item['requestTime'],
                    auditlogLink=item['auditlogLink']
                )
                count += 1
            return request_obj
        except Exception as e:
            print("Error: " + str(e))
            if request['Message'] == 'Invalid API key':
                print("Message: " + request['Message'] + "Check your API Key/Datacenter DC1 is EU and DC2 is US")

    # Get request by ID as JSON
    def get_request_id(self, id: int):
        url = self.url + 'request/' + str(id)
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        request = response.json()
        
        try:
            request_obj = ABRRequestRequestsObject(
                scanResults=request['scanResults'],
                id=request['id'],
                traceNo=request['traceNo'],
                settingsName=request['settingsName'],
                runType=request['type'],
                typeCode=request['typeCode'],
                status=request['status'],
                statusCode=request['statusCode'],
                application_file=request['application']['file'],
                application_name=request['application']['name'],
                application_vendor=request['application']['vendor'],
                application_version=request['application']['version'],
                application_sha256=request['application']['sha256'],
                application_scanResult=request['application']['scanResult'],
                application_scanResultCode=request['application']['scanResultCode'],
                application_threat=request['application']['threat'],
                application_virustotalLink=request['application']['virustotalLink'],
                user_account=request['user']['account'],
                user_fullname=request['user']['fullName'],
                user_email=request['user']['email'],
                user_phone=request['user']['phone'],
                computer_name=request['computer']['name'],
                computer_platform=request['computer']['platform'],
                computer_platformCode=request['computer']['platformCode'],
                computer_make=request['computer']['make'],
                computer_model=request['computer']['model'],
                reason=request['reason'],
                approvedBy=request['approvedBy'],
                approvedByEmail=request['approvedByEmail'],
                deniedReason=request['deniedReason'],
                deniedBy=request['deniedBy'],
                deniedByEmail=request['deniedByEmail'],
                requestTime=request['requestTime'],
                auditlogLink=request['auditlogLink']
            )
            return request_obj
        except Exception as e:
            print("Error: " + str(e))
            if request['Message'] == 'Invalid API key':
                print("Message: " + request['Message'] + "Check your API Key/Datacenter DC1 is EU and DC2 is US")
    
    # Approve request by ID
    def approve_request_id(self, id: int):
        url = self.url + 'request/' + str(id)
        headers = {
            "apikey": self.api_key
        }
        requests.put(url, headers=headers)
        
    # Approve request by ID with approved by
    def approve_request_id_approvedby(self, id: int, approvedby: str):
        url = self.url + 'request/' + str(id) + '?approvedby=' + approvedby
        headers = {
            "apikey": self.api_key
        }
        requests.put(url, headers=headers)
    
    # Deny request by ID
    def deny_request_id(self, id: int):
        url = self.url + 'request/' + str(id)
        headers = {
            "apikey": self.api_key
        }
        requests.delete(url, headers=headers)
        
    # Deny Request by ID with denied by and reason
    def deny_request_id_reason_deniedby(self, id: int, deniedby: str, reason: str):
        url = self.url + 'request/' + str(id) + '?deniedby=' + deniedby + '&reason=' + reason
        headers = {
            "apikey": self.api_key
        }
        requests.delete(url, headers=headers)
        
    # Deny Request by ID with denied by
    def deny_request_id_deniedby(self, id: int, deniedby: str):
        url = self.url + 'request/' + str(id) + '?deniedby=' + deniedby
        headers = {
            "apikey": self.api_key
        }
        requests.delete(url, headers=headers)
        
    # Deny Request by ID with reason
    def deny_request_id_reason(self, id: int, reason: str):
        url = self.url + 'request/' + str(id) + '?reason=' + reason
        headers = {
            "apikey": self.api_key
        }
        requests.delete(url, headers=headers)
    
# /events - Events API extension
    # Get all events as JSON
    def get_events(self, limit: int=10000, offset: int=0):
        url = self.url + 'events?limit=' + str(limit) + '&offset=' + str(offset)
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        events = response.json()
        event_obj = {}
        count = 0
        # Error Checking debugging issue with Users seeing issues when using the wrong Datacenter
        try:
            for item in events:
                event_obj[count] = ABRRequestEventObjects(
                    id=item['id'],
                    eventCode=item['eventCode'],
                    eventLevel=item['eventLevel'],
                    eventText=item['eventText'],
                    eventTime=item['eventTime'],
                    eventTimeUTC=item['eventTimeUTC'],
                    computerName=item['computerName'],
                    userAccount=item['userAccount'],
                    userName=item['userName'],
                    alertAccount=item['alertAccount'],
                    auditLogURL=item['auditLogURL'],
                    rollback=item['rollback'],
                    additionalData=item['additionalData'],
                    application_file=item['application']['file'],
                    application_path=item['application']['path'],
                    application_name=item['application']['name'],
                    application_vendor=item['application']['vendor'],
                    application_version=item['application']['version'],
                    application_sha256=item['application']['sha256']
                )
                count += 1
            return event_obj
        except Exception as e:
            print("Error: " + str(e))
            if events['Message'] == 'Invalid API key':
                print("Message: " + events['Message'] + " Check your API Key/Datacenter DC1 is EU and DC2 is US")
    
    # Get event by ID as JSON
    def get_events_id(self, id: int):
        url = self.url + 'events/' + str(id)
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        events = response.json()
        try:
            event_obj = ABRRequestEventObjects(
                id=events['id'],
                eventCode=events['eventCode'],
                eventLevel=events['eventLevel'],
                eventText=events['eventText'],
                eventTime=events['eventTime'],
                eventTimeUTC=events['eventTimeUTC'],
                computerName=events['computerName'],
                userAccount=events['userAccount'],
                userName=events['userName'],
                alertAccount=events['alertAccount'],
                auditLogURL=events['auditLogURL'],
                rollback=events['rollback'],
                additionalData=events['additionalData'],
                application_file=events['application']['file'],
                application_path=events['application']['path'],
                application_name=events['application']['name'],
                application_vendor=events['application']['vendor'],
                application_version=events['application']['version'],
                application_sha256=events['application']['sha256']
            )
            return event_obj
        except Exception as e:
            print("Error: " + str(e))
            if events['Message'] == 'Invalid API key':
                print("Message: " + events['Message'] + " Check your API Key/Datacenter DC1 is EU and DC2 is US")
                
    # Get all events of a certain computer, by computer name
    def get_event_computer(self, computername: str):
        url = self.url + 'computers/' + computername + "/events"
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        events = response.json()
        event_obj = {}
        count = 0
        
        try:
            for item in events:
                event_obj[count] = ABRRequestEventObjects(
                    id=item['id'],
                    eventCode=item['eventCode'],
                    eventLevel=item['eventLevel'],
                    eventText=item['eventText'],
                    eventTime=item['eventTime'],
                    eventTimeUTC=item['eventTimeUTC'],
                    computerName=item['computerName'],
                    userAccount=item['userAccount'],
                    userName=item['userName'],
                    alertAccount=item['alertAccount'],
                    auditLogURL=item['auditLogURL'],
                    rollback=item['rollback'],
                    additionalData=item['additionalData'],
                    application_file=item['application']['file'],
                    application_path=item['application']['path'],
                    application_name=item['application']['name'],
                    application_vendor=item['application']['vendor'],
                    application_version=item['application']['version'],
                    application_sha256=item['application']['sha256']
                )
                count += 1
            return event_obj
        except Exception as e:
            print("Error: " + str(e))
            if events['Message'] == 'Invalid API key':
                print("Message: " + events['Message'] + " Check your API Key/Datacenter DC1 is EU and DC2 is US")
                    
    # Get all events of a certain user, by username
    def get_events_user(self, username: str):
        url = self.url + 'users/' + username + "/events"
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        events = response.json()
        event_obj = {}
        count = 0
        
        try:
            for item in events:
                event_obj[count] = ABRRequestEventObjects(
                    id=item['id'],
                    eventCode=item['eventCode'],
                    eventLevel=item['eventLevel'],
                    eventText=item['eventText'],
                    eventTime=item['eventTime'],
                    eventTimeUTC=item['eventTimeUTC'],
                    computerName=item['computerName'],
                    userAccount=item['userAccount'],
                    userName=item['userName'],
                    alertAccount=item['alertAccount'],
                    auditLogURL=item['auditLogURL'],
                    rollback=item['rollback'],
                    additionalData=item['additionalData'],
                    application_file=item['application']['file'],
                    application_path=item['application']['path'],
                    application_name=item['application']['name'],
                    application_vendor=item['application']['vendor'],
                    application_version=item['application']['version'],
                    application_sha256=item['application']['sha256']
                )
                count += 1
            return event_obj
        except Exception as e:
            print("Error: " + str(e))
            if events['Message'] == 'Invalid API key':
                print("Message: " + events['Message'] + " Check your API Key/Datacenter DC1 is EU and DC2 is US")
     
    # Get Errors by Code
    def get_events_errorCode(self, limit: int = 10000, offset: int = 0, errorCode = ABREventCodes.Support_Assist_Initiated):
        events = None
        if errorCode not in ABREventCodes:
            url = self.url + 'events?limit=' + str(limit) + '&offset=' + str(offset) + '&code=' + str(errorCode)
            headers = {
                "apikey": self.api_key
            }
            response = requests.get(url, headers=headers)
            events = response.json()
        else:
            errorCode: int = errorCode.value
            url = self.url + 'events?limit=' + str(limit) + '&offset=' + str(offset) + '&code=' + str(errorCode)
            headers = {
                "apikey": self.api_key
            }
            response = requests.get(url, headers=headers)
            events = response.json()
        event_obj = {}
        count = 0
        
        try:
            for item in events:
                event_obj[count] = ABRRequestEventObjects(
                    id=item['id'],
                    eventCode=item['eventCode'], # This is Consistant because this only returns the same event.
                    eventLevel=item['eventLevel'],
                    eventText=item['eventText'],
                    eventTime=item['eventTime'],
                    eventTimeUTC=item['eventTimeUTC'],
                    computerName=item['computerName'],
                    userAccount=item['userAccount'],
                    userName=item['userName'],
                    alertAccount=item['alertAccount'],
                    auditLogURL=item['auditLogURL'],
                    rollback=item['rollback'],
                    additionalData=item['additionalData'],
                    application_file=item['application']['file'],
                    application_path=item['application']['path'],
                    application_name=item['application']['name'],
                    application_vendor=item['application']['vendor'],
                    application_version=item['application']['version'],
                    application_sha256=item['application']['sha256']
                )
                count += 1
            return event_obj  
        except Exception as e:
            print("Error: " + str(e))
            if events['Message'] == 'Invalid API key':
                print("Message: " + events['Message'] + " Check your API Key/Datacenter DC1 is EU and DC2 is US")

# /pin - Pin Code API extension (Extension of the Invetory API)
    # Get pin code as String from the computer's Inventory by computer id
    def get_pin_id(self, id: int):
        url = self.url + 'inventory/' + str(id) + '/pin'
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        pin = response.json()
        return pin
    
    # Get pin code as String from the computer's Inventory by computer name
    def get_pin_computer(self, computername: str):
        url = self.url + 'inventory/' + computername + '/pin'
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        pin = response.json()
        return pin
    
