from dataclasses import dataclass, field
@dataclass
class person:
    name:str
    age:int = field(defult=0)
    def __post_init__(self):
        if self.age<0:
            raise ValueError("age can't be negative")
Person=person("nedhy", 27)
print(Person)