import requests
from enum import Enum
import datetime

class ABRRequestInventoryObject:
    def __init__(self, id, name, inventoryDate='', inventoryAvailable='', clientVerion='', os=''):
        self.id = id
        self.name = name
        self.inventoryDate = inventoryDate
        self.inventoryAvailable = inventoryAvailable
        self.clientVersion = clientVerion
        self.os = os
        
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
        return inventory
    # Get inventory item by ID as JSON
    def get_inventory_id(self, id: int):
        url = self.url + 'inventory/' + str(id)
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
        inventory_id = response.json()
        return inventory_id
    # Get inventory item by computer as JSON
    def get_inventory_computer(self, computername: str):
        url = self.url + 'computers/' + computername + "/inventory"
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url, headers=headers)
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
        # Convert days to "2024-08-27T14:04:14.887" format
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
        # Filter inventory items by availability and date in a single pass
        if unavailable:
            for item in inventory:
                if not item['inventoryAvailable'] or (item['inventoryAvailable'] and item['inventoryDate'] < days):
                    inv_obj[count] = ABRRequestInventoryObject(
                        item['id'], 
                        item['name'], 
                        item['inventoryDate'], 
                        item['inventoryAvailable'], 
                        item['abrClientVersion'], 
                        item['operatingSystem']
                    )
                    count += 1
        else:
            for item in inventory:
                if item['inventoryAvailable'] and item['inventoryDate'] < days:
                    inv_obj[count] = ABRRequestInventoryObject(
                        item['id'], 
                        item['name'], 
                        item['inventoryDate'], 
                        item['inventoryAvailable'], 
                        item['abrClientVersion'], 
                        item['operatingSystem']
                    )
                    count += 1
        return inv_obj
    
    
