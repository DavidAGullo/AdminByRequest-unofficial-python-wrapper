from adminbyrequest import AdminByRequest, ABRDatacenter, ABRRequestInventoryObject

abr = AdminByRequest('APIKEY', datacenter=ABRDatacenter.dc2)

UserComputer: str = ''   # User's Full Name or first name to filter inventory results, leave blank to get all inventory items
Max_Take: int = 50  # Max number of inventory items to return, max is 10000 per request

# Get 200 Inventory items
inventory_items : ABRRequestInventoryObject = abr.get_inventory(take=Max_Take)
for item in range(len(inventory_items)):
    # Only if the Computer User's name starts with XXXX
    if UserComputer in str(inventory_items[item].user_fullname): # Custom String parameter filersts such as startswith, endswith, contains, etc
        print(f"Inventory ID: {inventory_items[item].id} - Computer Name: {inventory_items[item].name} - Pin Code: {abr.get_uninstall_pin(id=inventory_items[item].id)}")

