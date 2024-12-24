import time
def countdown(seconds):
    while seconds >0:
        print(f"time left {seconds} seconds")
        time.sleep(1)
        seconds -=1
    print("times up!")
countdown(10)
#useer input for coundown time
try:
    user_input=int(input("enter the countdown number in seconds: "))
    if user_input>0:
        countdown(user_input)
    else:
        print("enter a positive number: ")
except ValueError:
    print("invalid input please input a integer value")