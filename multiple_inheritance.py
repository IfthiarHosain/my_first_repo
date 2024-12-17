class employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("the name of employee:",self.name)
class dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print("the dance is:",self.dance)
class employeedancer(employee,dancer):
    def __init__(self, name,dance):
        self.name=name
        self.dance=dance
o=employeedancer("rohit","hiphop")
print(o.name)
print(o.dance)
o.show()
print(employeedancer.mro())
        
    