class Node:
    def __init__(self,data) -> None:
        self.data= data
        self. next= None
class linked_list:
    def __init__(self) -> None:
        self.head=None
    def disply(self):
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next
            print()        
    def insert(self,data):
        new_Node=Node(data)
        if not self.head:
            self.head=new_Node
        else: 
            current=self.head
            while current.next:
              current=current.next
            current.next=new_Node
    def delete(self,data):
        if not self.head:
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        current=self.head
        prev=None
        while current and current.data!=data:
            prev=current
            current=current.next
        if current:
            prev.next=current.next
linklist=linked_list()
linklist.insert(1)
linklist.insert(5)
linklist.insert(10)
print("initial linked list")
linklist.disply()
linklist.insert(20)
print("after inserting a new node")
linklist.disply()
linklist.delete(5)
print("after deleting 5")
linklist.disply()





