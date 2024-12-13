class employee:
    def __init__(self,name,salary):
        self.name= name 
        self.salary= salary
    @classmethod
    def fromstr(cls,string):
        name,salary= string.split("-")
        return cls(name,int(salary))

string="kabbo-45000"
emp1=employee.fromstr(string)
print(emp1.name)
print(emp1.salary)

emp2=employee("Nedhy", 12000)
print(emp2.name)
print(emp2.salary)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def  fromstring(cls,string):
        name,age=string.split(",")
        return cls(name, int(age))
Person=person("shishir",27)
print (Person.name)
print(Person.age)      
print(Person.name,Person.age)  


class rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    @classmethod
    def square(cls,size):
        return cls(size,size)
r=rectangle.square(10)
print(r.height)
print(r.width)
