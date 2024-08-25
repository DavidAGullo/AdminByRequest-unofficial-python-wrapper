import requests

class AdminByRequest:
    def __init__(self, apikey):
        self.api_key = apikey
        self.url = 'https://dc2api.adminbyrequest.com/'
        
# /auditlog - Audit Log API extension

    def get_all_audit_logs(self):
        audit_logs : str = []
        count = 0
        url = self.url + 'auditlog'
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        for log in response.json():
            audit_logs[log] = "Entry: " + str(count) + " | User: " + log['user']['account'] + log['elevatedApplications']['name']
            count+=1
        return audit_logs
        