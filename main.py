numbers=[5,10,15,20]
threshold=12
average= sum(numbers)/len(numbers)
if (avg:=average)>threshold:
    print(f"average is {avg} is above of threshold")
else:
    print(f"average is {avg} is lower then threshold")