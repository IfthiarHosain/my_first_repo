# factorial=1
# num=2
# if num<0:
#     print("there is no factorial for negative numbers: ")
# elif num==0:
#     print("the factorial of zero is: 1")
# else:
#     for i in range(1,num+1):
#      factorial=factorial*i
#     print(f"the factorial {num} of {factorial}")
# recursive way
# def factorial(n):
    # if (n==0 or n==1):
    #     return 1
    # else:
    #     return n*factorial(n-1)
# turnery operator
def factorial(n):
    return 1 if (n==0 or n==1) else n*factorial(n-1)
num=5
print(f"the factorial {num} of {factorial(num)}")