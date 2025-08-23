from adminbyrequest import AdminByRequest, ABRDatacenter # This imports the AdminByRequest class (required to interact with the API) 
                                                         # and the ABRDatacenter enum (to specify the datacenter)

abr = AdminByRequest('APIKEY', ABRDatacenter.dc2) # Insert your API key here and Modify the datacenter if needed (DC1 is EU and DC2 is US)

audit_runAs = abr.get_auditlog(take=100, days=730, a_type='app') # Get the first 100 RunAs Application Audit Logs from the last 2 years
audit_session = abr.get_auditlog(take=100, days=730, a_type='session') # Get the first 100 Admin Session Audit Logs from the last 2 years
audit_logs = abr.get_auditlog(take=100, days=730) # Get the first 100 Audit Logs from the last 2 years (all types)

audit = audit_session # You can change this to audit_runAs or audit_logs to see different types of logs

for entry in audit:
    print(f"Entry: {entry+1} - Audit ID: {audit[entry].id}; Application: {audit[entry].application_name}; User: {audit[entry].user_account}")
    # Example Output:
    # Entry: 1 - Audit ID: 123456; Application: AdminByRequest; User:DOMAIN\BobT
    # Entry: 2 - Audit ID: 123457; Application: AdminByRequest; User:DOMAIN\AliceS
