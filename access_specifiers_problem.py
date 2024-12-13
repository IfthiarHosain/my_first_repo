class parent:
    def __init__(self):
        self.__private= "parent is private"
class child(parent):
    def __init__(self):
        super().__init__()
        self.__private ="child is private"
obj= child()
print(obj._parent__private)
print(obj._child__private)

class base:
    def __init__(self):
        self._protected = "its protected"
    @property
    def protected(self):
        return self._protected
obj=base()
print(obj.protected)

class example:
    def __init__(self):
        self.__data = "hidden data"
    def get_data(self):
        return self.__data
obj=example()
print(obj.get_data())
