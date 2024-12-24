import winreg
key=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer")
value,_=winreg.QueryValueEx(key,"link")
print("Register Value",value)
winreg.CloseKey(key)