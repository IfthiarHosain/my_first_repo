from datetime import date,datetime
class person:
    def __init__(self,name,country,date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth= datetime.strptime(date_of_birth,"%d/%m/%Y").date()
    def calculate_age(self):
        today=date.today()
        age=today.year - self.date_of_birth.year
        if today<date(today.year,self.date_of_birth.month,self.date_of_birth.day):
            age-=1
        return age
person1=person("shishir","Bangladesh","12/08/1997")
person2=person("Hafiz","pakistan","15/02/1990")
person3=person("Alen","America","25/01/2000")
# print(person1)
print("Name: ",person1.name)
print("country: ",person1.country)
print("date of birth: ",person1.date_of_birth)
print("Age: ",person1.calculate_age())
# print(person2)
print("Name: ",person2.name)
print("country: ",person2.country)
print("date of birth: ",person2.date_of_birth)
print("Age: ",person2.calculate_age())
# print(person3)
print("Name: ",person3.name)
print("country: ",person3.country)
print("date of birth: ",person3.date_of_birth)
print("Age: ",person3.calculate_age())