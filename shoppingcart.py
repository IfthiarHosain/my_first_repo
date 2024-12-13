class shoppingcart():
    def __init__(self) -> None:
         self.items=[]
    def add_items(self,item_name,qunt):
         item=(item_name,qunt)
         self.items.append(item)
    def remove_items(self,item_name):
         for item in self.items:
              if item[0]==item_name:
                   self.items.remove(item)
                   break
    def calcutale_total(self):
         total=0
         for item in self.items:
              total+=item[1]
         return total
cart=shoppingcart()
cart.add_items("mango",100)
cart.add_items("papaya",1500)
cart.add_items('underware',2500)
print("the current items in cart: ")
for item in cart.items:
     print(item[0],"-",item[1])
totall_quantity=cart.calcutale_total()
print("total quantity: ", totall_quantity)
cart.remove_items("papaya")
print("updated items after removing papaya")
for items in cart.items:
     print(item[0],"-",item[1])
totall_quantity=cart.calcutale_total()
print("total quantity:", totall_quantity)