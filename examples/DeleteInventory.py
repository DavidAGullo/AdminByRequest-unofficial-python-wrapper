from adminbyrequest import AdminByRequest, ABRDatacenter # This imports the AdminByRequest class (required to interact with the API) however in this example we are not
                                                         # using the ABRDatacenter enum as we are specifying the datacenter directly in the AdminByRequest constructor       

abr = AdminByRequest('APIKEY', ABRDatacenter.dc2) # With ABRDatacenter you can specify the datacenter, here we are using 'dc2' which is US.
alt_abr = AdminByRequest('APIKEY', 'dc2') # Alternatively, you can specify the datacenter as a string directly, here we are using 'dc2' which is US.

# Get inventory items older than 20 days
days = 20 # Specify the number of days to look back for inventory items
inventory = alt_abr.get_inventory_by_date(days) # Get Anything Older than 20 days

# Count how many items were found and display their details
print(f"Found {len(inventory)} inventory items older than {days} days")
for item in inventory:
    print(f"Item: {inventory[item].id} - {inventory[item].name} - Last Seen: {inventory[item].inventoryDate}")

# Ask user for confirmation before deleting items
print("Would you like to delete these items? (y/n)")
confirm = input().strip().lower()
if confirm == 'y':
    for item in inventory:
        print(f"Deleting Item: {inventory[item].id} - {inventory[item].name}")
        alt_abr.delete_inventory_id(inventory[item].id)
    print("Deletion complete.")