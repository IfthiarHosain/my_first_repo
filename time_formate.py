import time
current_time=time.localtime()
formatted_time=time.strftime("%I:%M:%S:%p",current_time)
#formatted_time=time.strftime("%H:%M:%S", current_time) 
# for 24 hour clock formate
print("current time:", formatted_time)