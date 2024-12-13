class employee:
    company="Bata"
    def show(self):
        print(f"the name is {self.name} and the company name is {self.company}")
    @classmethod
    def changecompany(cls,newcompany):
        cls.company=newcompany


emp1=employee()
emp1.name="Nedhy"
emp1.show()
emp1.changecompany("Apex")
emp1.show()
print(employee.company)

