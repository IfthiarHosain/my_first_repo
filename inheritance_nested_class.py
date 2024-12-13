class employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showdetails(self):
        print(f"Name of a employee: {self.name} id is  {self.id}")
class programmer(employee):
    def showlanguage(self):
        print("the default language is python")
class chodao(programmer):
    def showage(self,age):
        self._age = age
        if age<0:
            print("age cannot be negative")
        else:
            print(f"age: {age}")
class mahi(chodao):
    def showgali(self,gali):
        self._gali= gali
        print(f"mahi has told you this {gali}")
class shawon(mahi):
    def showsalis_name(self,name):
        self._name = name
        print(f"shalis name {name}")

e1= employee("tulsi das", 520)
e1.showdetails()
e2= programmer("hogamara",1603)
e2.showdetails()
e2.showlanguage()
e3=chodao("rani",420)
e3.showdetails()
e3.showlanguage()
e3.showage(18)
e4=mahi("gudmarani",500)
e4.showdetails()
e4.showlanguage()
e4.showage(24)
e4.showgali("chutmarani")
shali=shawon("amina",315)
shali.showdetails()
shali.showlanguage()
shali.showage(20)
shali.showgali("khankimagi")
shali.showsalis_name("fatema")