class employee:
    def __init__(self,name,gali):
        self.name = name
        self.gali=gali
    
    def __len__(self):
        i=0
        for c in self.name:
            i= i+1
        return i
    def __str__(self):
        return f"name of the employee is '{self.name}'"
    def __repr__(self): #when __str__ dont work or dont exist 
        #then __repr__ will run or work
        return f" employee('{self.name}')"
    def __call__(self,gali):
        self.gali= gali
        print (f"you are a {self.gali}")        
emp=employee("nedhy","madari")
print(len(emp))
emp2=employee("Akash","sudani")
print(len(emp2))