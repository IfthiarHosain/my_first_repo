import win32serviceutil
service_name="spooler"
win32serviceutil.StartService(service_name)
print(f" {service_name} service started sucessfully")