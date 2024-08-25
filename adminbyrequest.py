from dotenv import load_dotenv
import requests

class AdminByRequest:
    def __init__(self, apikey):
        load_dotenv()
        self.api_key = apikey
        self.headers
        self.url = 'https://dc1api.adminbyrequest.com/'
        
# /auditlog - Get the audit log API stuff
    def auditlog():
        pass