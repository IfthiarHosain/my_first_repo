class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        print("the sound by the animal")
class cat(Animal):
    def __init__(self, name, breed="cat"):
        self.name=name
        self.breed= breed
    def make_sound(self):
        print("meaw")
    def food_habit(self,foodname):
        self.foodname=foodname
        return ("food name:", foodname)

c=Animal("pussy","persian")
c1=cat("utsho","desi")
sound=c.make_sound()
food=c1.food_habit("cat food")
d=c1.make_sound()
print(sound)
print(food) 
print(d)   

