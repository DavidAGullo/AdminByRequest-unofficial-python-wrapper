from adminbyrequest import AdminByRequest, ABRDatacenter

abr = AdminByRequest('APIKEY', datacenter=ABRDatacenter.dc2)

EntriesPerPage = 10 # Take
PagesToFetch = 5 # Pagination | Total Entries = (EntriesPerPage - 1) * PagesToFetch + 1

    # Example Output:
    # --- Page 1 ---
    # Entry: 1 - Audit ID: 125150313; Date:2025-08-21T17:00:30; Application: Google Chrome; User: FENEX\BOBT
    # Entry: 2 - Audit ID: 125160313; Date:2025-08-21T17:03:30; Application: Google Chrome; User: FENEX\BOBT
    # ...
    # --- Page 2 ---
    # Entry: 1 - Audit ID: 123454626; Date:2025-08-21T17:00:30; Application: AdminByRequest; User:DOMAIN\CharlieD
    # Entry: 2 - Audit ID: 123473367; Date:2025-08-21T17:00:30; Application: AdminByRequest; User:DOMAIN\EveM
    # ...
    # Note: The Audit IDs will be different in your output as they are unique to each log entry.


def fetch_auditlogs(start_id=None, take=10):
    if start_id:
        return abr.get_auditlog(take=take, start_id=start_id)
    else:
        return abr.get_auditlog(take=take)
        

# Initial Fetch of Audit Logs (without start_id) to find the last ID for pagination
audit_logs_intial = fetch_auditlogs(take=EntriesPerPage)
for page in range(PagesToFetch):
    print(f"--- Page {page+1} ---")
    for entry in range(len(audit_logs_intial)):
        print(f"Entry: {entry+1} - Audit ID: {audit_logs_intial[entry].id}; Date:{audit_logs_intial[entry].requestTime}; Application: {audit_logs_intial[entry].application_name}; User: {audit_logs_intial[entry].user_account}")
    # Fetch the next page using the last ID from the current page
    last_id = audit_logs_intial[len(audit_logs_intial)-1].id
    # Starts the next fetch from the last ID of the previous fetch
    audit_logs_intial = fetch_auditlogs(start_id=last_id, take=EntriesPerPage)