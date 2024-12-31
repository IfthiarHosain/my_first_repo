import time
input("please enter to start the stop watch..")
start_time=time.time()
input("please enter to stop the storwatch")
end_time=time.time()
elaps_time=end_time-start_time
print(f"elaps time: {elaps_time:.2f} seconds")
