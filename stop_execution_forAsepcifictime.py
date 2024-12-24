import time
def countdown_with_intervels(seconds):
    print("count down with different intervels:")
    for i in range(seconds,0,-1):
        print(f"timeleft{i} seconds")
        if i >5:
            time.sleep(2)
        else:
            time.sleep(1)
    print("times up")
try:
    user_input=int(input("enter the countdown time in seconds: "))
    if user_input>0:
        countdown_with_intervels(user_input)
    else:
        print("please enter a positive number")
except ValueError:
    print("invalid input! please enter an integer value")