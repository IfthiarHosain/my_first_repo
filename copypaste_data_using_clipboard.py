import win32clipboard
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText("Hello chutmarani")
win32clipboard.CloseClipboard()
#to retrive data
win32clipboard.OpenClipboard()
data=win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
print("Clipboard Content:", data)

