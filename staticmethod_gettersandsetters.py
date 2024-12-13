class person:
    def __init__(self,age):
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        self.validate_age(value)
        self._age=value
    @staticmethod
    def validate_age(value):
        if value<0:
            raise ValueError("age cannot be negative")


