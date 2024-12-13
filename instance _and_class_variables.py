class employee:
    companyname= "HP"
    chairmanname="Harun Uncle"
    numberofemployess=0
    def __init__(self,name):
        self.name= name
        self.raise_amount=0.02
        employee.numberofemployess +=1
    
    def showdetails(self):
        print(f"my name is  {self.name} in the company {self.companyname} and the chairmans name is {self.chairmanname} the raise amount in sized {self.numberofemployess} of company{self.raise_amount}" )
emp1=employee("nedhy")
emp1.raise_amount= 0.03
emp1.companyname="Apple Bangladesh"
emp1.showdetails()
employee.companyname= "google"
print(employee.companyname)

emp2=employee("Harry")
emp2.companyname="microsoft"
emp2.showdetails()
emp3=employee("siam")
emp3.showdetails()