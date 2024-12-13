class parent:
    def parent_method(self):
        print("this is the parent class")
class child(parent):
    def parent_method(self):
        print("happy")
        super().parent_method()
    def child_methods(self):
        print("this is the child class")
        super().parent_method()
child_object=child()
child_object.child_methods()
child_object.parent_method()

class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class programmer(employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang= lang
shojon=employee("shojon gupta",425)
harry=programmer("harry",1236,"python")
print(shojon.name)
print(shojon.id)
print(harry.name)
print(harry.id,harry.lang)


