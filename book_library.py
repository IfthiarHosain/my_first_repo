class library:
    def __init__(self):
       self.no_ofbooks=0
       self.books=[]
    def addbooks(self,book):
        self.books.append(book)
        self.no_ofbooks=len(self.books)
    def showdetails(self):
        print(f"the number of book library has {self.no_ofbooks} books.The books are")
        for book in self.books:
            print(book)  
li1=library()
li1.addbooks("Shonar tori")
li1.addbooks("Fault in our starts")
li1.addbooks("Notebook")
li1.addbooks("Srabon megher din")
li1.showdetails()