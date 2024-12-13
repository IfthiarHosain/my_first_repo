a=int(input("Enter the Number: "))
i=2
n=0
while i<a:
    if a%i==0:
        n=1
        break
    i=i+1
if n==0:
      print(a,"is a prime number!!")
else:
     print(a,"is not a prime number; its a composite number")