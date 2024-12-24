import time
epoch_time=time.time()
print(f"Epoch time {epoch_time}")
readable_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(epoch_time))
print("human readable time:", readable_time)
print(f"Comverted back to epoch time: {back_to_epoch}" )
struck_time=time.strptime(readable_time,"%Y-%m-%d %H:%M:%S")
back_to_epoch=time.mktime(struck_time)
back_to_epoch=time.mktime(struck_time)
back_to_epoch=time.mktime(struck_time)
def convert_epoch_to_datetime(epoch_timestamp):
    try:
        converted_time=time.localtime(epoch_timestamp)
        formated_time=time.strftime("%A, %B %d, %Y %I:%M:%S %p", converted_time)
        print(f"converted Date and time: {formated_time}")
    except Exception as e:
        print("Error", e)
    try:
        user_input=float(input("enter epoch timestamp (e.g., 1672531199): "))
        convert_epoch_to_datetime(user_input)
    except ValueError:
        print("invalid input! please enter the numeric value for the epoch timestamp")
c=convert_epoch_to_datetime(1735072314.0)
print (c)