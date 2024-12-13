class area:
    def __init__(self,name,road_number):
        self._name= name
        self._road_number=road_number
    @property 
    def road_number(self):
        return self._road_number
    @road_number.setter
    def road_number(self,value):
        if value<0:
            raise ValueError("road number cannot be Negative")
        self._road_number=value
Area=area("dolaiper",20)
print(Area.road_number)
Area.road_number=-30
print (Area.road_number)


