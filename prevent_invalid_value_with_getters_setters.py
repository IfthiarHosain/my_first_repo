class person:
    def __init__(self,age):
        self.age=None
        self.set_age(age)
    def get_age(self):
        return self._age
    def set_age(self,value):
        if value<0:
            raise ValueError("Age cannot be Negative Number")
        self._age=value
Person= person(25)
Person= person(-20)

