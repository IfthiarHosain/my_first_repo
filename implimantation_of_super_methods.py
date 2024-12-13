class employee:
    def __init__(self,name,age,id,salary):
        self.name=name
        self.age=age
        self.id=id
        self.salary=salary
    def info(self):
        print(f"employee informatiron : {self.name},{self.age},{self.id},{self.salary}")
class address(employee):
    def colony(self,address):
     self.address=address 
     return ("the address is", {self.address},super().info()) 
e=address("mahesh",25,1603,25000)
print(e.colony("jatrabari"))