import time
current_time=time.localtime()
formatted_datetime=time.strftime("%A, %B %d  %Y %I:%M:%S:%p", current_time)
print (f"current time: {formatted_datetime}")