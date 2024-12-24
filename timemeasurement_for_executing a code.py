import time
start_time=time.time()
for i in range(1,1000000):
    _=i*i
    
end_time=time.time()
elaps_time= (end_time - start_time)
print(f"program executed in {elaps_time:.2f} seconds")
class employee():
    def show_details(self,name,id):
        self.name=name
        self.id=id
        print(f"Employee name {self.name}, id {self.id}")
e=employee()
e.show_details("shuvam",205)
