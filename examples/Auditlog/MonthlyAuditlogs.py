from adminbyrequest import AdminByRequest, ABRDatacenter

# Months Enums
class Month:
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12

abr = AdminByRequest('APIKEY', datacenter=ABRDatacenter.dc2)

# Monthly Reporting (Get this Months Audit Logs)
reportMonth = Month.March
reportYear = "2025"
_take = 100

def get_last_day(month, year) -> int:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:  # February
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
        
# Date Format: YYYY-MM-DD (We alway know the first day of the month is 01, so we just need to get the last day of the month with get_last_day function)
audit_logs = abr.get_auditlog(
    take=_take, 
    startdate=(f"{int(reportYear)}-{reportMonth:02d}-01"), 
    enddate=(f"{reportYear}-{reportMonth:02d}-{get_last_day(reportMonth, int(reportYear))}"))

for entry in range(len(audit_logs)):
    print(f"Entry: {entry+1} - Audit ID: {audit_logs[entry].id}; Date:{audit_logs[entry].requestTime}; Application: {audit_logs[entry].application_name}; User: {audit_logs[entry].user_account}")
    # Example Output:
    # Entry: 1 - Audit ID: 123456; Date:2025-03-14T10:42:28; Application: AdminByRequest; User:DOMAIN\BobT
    # Entry: 2 - Audit ID: 123457; Date:2025-03-14T10:42:28; Application: AdminByRequest; User:DOMAIN\AliceS