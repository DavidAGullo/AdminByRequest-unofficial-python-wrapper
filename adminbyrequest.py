import requests

class AdminByRequest:
    def __init__(self, apikey):
        self.api_key = apikey
        self.url = 'https://dc2api.adminbyrequest.com/'
        
# /auditlog - Audit Log API extension

    # Get all audit logs as JSON
    def get_auditlog(self):
        url = self.url + 'auditlog'
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        auditlogs = response.json()
        return auditlogs
    
    # Get audit log by ID as JSON
    def get_auditlog_id(self, id: int):
        url = self.url + 'auditlog/' + str(id)
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        auditlog_id = response.json()
        return auditlog_id
    
    # Get audit log by computer as JSON
    def get_auditlog_computer(self, computername: str):
        url = self.url + 'computers/' + computername + "/auditlog"
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        return response.json()
    
    # Get audit log by user as JSON
    def get_auditlog_username(self, username: str):
        url = self.url + 'users/' + username + "/auditlog"
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        return response.json()
    
    # Get the timeNow Value which will be used to calculate until the next delta [This number increases by second]
    def get_auditlogs_delta(self):
        url = self.url + 'auditlog/delta'
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        time = data['timeNow']
        return time
    
