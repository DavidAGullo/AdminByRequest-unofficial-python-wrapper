from adminbyrequest import AdminByRequest, ABRDatacenter

abr = AdminByRequest('APIKEY', datacenter=ABRDatacenter.dc2)

computername = 'TESTMACHINE-ENT'
pin_1 = '123456'

results = (abr.get_second_pin(computername=computername, pin_one=pin_1))

print(results)