class queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("can't dequeue an empty queue")
    def is_empty(self):
        return len(self.items)==0
q=queue()
q.enqueue(50)
q.enqueue(25)
q.enqueue(30)
q.enqueue(35)
q.enqueue(15)
print("current Queue:", q.items)
dequeue_items=q.dequeue()
print("dequeue items", dequeue_items)
dequeue_items=q.dequeue()
print("dequeue items",dequeue_items)


