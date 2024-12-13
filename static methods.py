class math:
    def __init__(self,num) -> None:
        self.num = num
    def addtonum(self,n):
        self.num= self.num + n
    @staticmethod 
    def multiply(a,b):
        return a*b 
result=math(15)
print(result.num)
result.addtonum(20)
print(result.num)
result.addtonum(35)
print(result.num)
print(math.multiply(3,2))
