class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return (f"{self.i}i +{self.j}j +{self.k}k")
    def add(self,x):
        return  vector(self.i+x.i,self.j+x.j,self.k+x.k)
    
v=vector(4,5,6)
v2=vector(5,7,8)
print(v)
print(v2)
print(v.add(v2))
print(type(v.add(v2)))