N=int(input("Ente a value: "))
if N % 2 !=0:
    print("wired!")
elif N %2 == 0 and 2<=N<=6:
    print("not wired!")
elif N %2 == 0 and 6<=N<=20:
     print("wired")
elif N %2 == 0 and N >20:
     print("Not wired")   
else:
     print("fuck you!!")



