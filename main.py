class Mynumber:
    def __init__(self,value):
        self.value=value
    def __sub__(self,other):
        if isinstance(other,Mynumber):
            return (self.value-other.value)
        else:
            raise TypeError (f"Unsupported type for subtraction", {type(other)})
    def __repr__(self):
        return(f"mynumber {self.value}")
num1=Mynumber(20)
num2=Mynumber(25)
result= num1-num2
print(result)