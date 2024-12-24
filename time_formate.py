import time
current_time=time.localtime()
formatted_time=time.strftime("%I:%M:%S:%p",current_time)
print("current time:", formatted_time)