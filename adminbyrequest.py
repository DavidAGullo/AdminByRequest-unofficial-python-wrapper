import requests

class AdminByRequest:
    def __init__(self, apikey):
        self.api_key = apikey
        self.url = 'https://dc2api.adminbyrequest.com/'
        
# /auditlog - Audit Log API extension

    # Get all audit logs as JSON
    def get_all_audit_logs(self):
        audit_logs = []
        url = self.url + 'auditlog'
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        return audit_logs
    
    # Get audit log by ID as JSON
    def get_audit_log_by_id(self, id):
        audit_log = []
        url = self.url + 'auditlog/' + str(id)
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        return audit_log
    
    # Get audit log by computer as JSON
    def get_audit_log_by_computer(self, computername):
        audit_logs = []
        url = self.url + 'computers/' + computername + "/auditlog"
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        return audit_logs
    
    # Get audit log by user as JSON
    def get_audit_log_by_user(self, username):
        audit_logs = []
        url = self.url + 'users/' + username + "/auditlog"
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        return audit_logs
    
    # Get the timeNow Value which will be used to calculate until the next delta [This number increases by second]
    def get_delta_audit_logs(self):
        audit_logs = []
        url = self.url + 'auditlog/delta'
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        return audit_logs["timeNow"]
    
