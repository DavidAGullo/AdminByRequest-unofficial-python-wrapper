from adminbyrequest import AdminByRequest, ABRDatacenter, ABR_Status, ABRRequestRequestsObject

abr = AdminByRequest('APIKEY', datacenter=ABRDatacenter.dc2)

User_Email: str = 'API@email.com'   # User Email this will show as the approver/denier in the portal and email notifications
                                    # Make sure this email is associated with an AdminByRequest Admin account in your portal

def fetch_latest_request(Status=ABR_Status.pending):
    return abr.get_requests(take=1, status=Status)

# Main code
latest_pending_request : ABRRequestRequestsObject = fetch_latest_request(Status=ABR_Status.pending) # or 'Pending' for status as string form
while True:
    # Deploy the latest pending request (error handling if no pending requests)
    if not latest_pending_request:
        print("No pending requests found. Exiting the program.")
        break
    print(f"Pending Request ID: {latest_pending_request[0].id} User: {latest_pending_request[0].user_account} Application: {latest_pending_request[0].application_name} User's Reason: {latest_pending_request[0].reason}")
    # Prompt user to confirm or decline
    user_input = input("Type 'a' to Approve, 'd' to Decline the request, or 'q' to Quit: ").strip().lower()
    if user_input == 'a':
        abr.approve_request(latest_pending_request[0].id, approvedby=User_Email)
        print(f"Request ID: {latest_pending_request[0].id} has been Approved.")
    elif user_input == 'd':
        # Prompt for a reason for declining
        reasoning = input("Enter a reason for declining the request: ").strip()
        abr.deny_request(latest_pending_request[0].id, deniedby=User_Email, reason=(f"Denied via API: {reasoning}"))
        print(f"Request ID: {latest_pending_request[0].id} has been Declined.")
    elif user_input == 'q':
        # User chose to quit
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please try again.")
        continue
    # Fetch the next latest pending request
    latest_pending_request = fetch_latest_request(Status=ABR_Status.pending)
    if not latest_pending_request:
        print("No more pending requests. Exiting the program.")
        break   
    print("\n")
    
# Example Output:
# Deploying Request ID: 123456 User: DOMAIN\BobT Application: AdminBy
# Type 'a' to Approve, 'd' to Decline the request, or 'q' to Quit: a
# Request ID: 123456 has been Approved.
# 
# Deploying Request ID: 123457 User: DOMAIN\AliceS Application: Google Chrome
# Type 'a' to Approve, 'd' to Decline the request, or 'q' to Quit: d
# Request ID: 123457 has been Declined.
# 
# Deploying Request ID: 123458 User: DOMAIN\CharlieD Application: Visual Studio
# Type 'a' to Approve, 'd' to Decline the request, or 'q' to Quit: q
# Exiting the program.      