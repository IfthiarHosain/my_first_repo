class Employee:
    def __init__(self) -> None:
        self.__roll_number = 1603
obj=Employee()
print(obj._Employee__roll_number)

class student:
   def __init__(self):
      self._name= "Nedhy"
   def  _fun_name(self):
      return "chodna"
class subject(student):
   def subject_name(self): 
      print("science")
obj1= student()
obj2=subject()
print(obj1._name)
print(obj1._fun_name())
print(obj2.subject_name())
print(obj2._fun_name())
print(obj2._name)
