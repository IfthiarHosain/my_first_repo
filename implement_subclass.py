import math
class shape:
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi*self.radius**2
    def calculate_perimeter(self):
        return 2*math.pi*self.radius
class rectangle(shape):
    def __init__(self,length,width) :
        self.length=length
        self.width=width
    def calculate_area(self):
        return self.length*self.width
    def calculate_perimeter(self):
        return 2*(self.length+ self.width)
class triangle(shape):
    def __init__(self,base,height,side1,side2,side3):
        self.base = base
        self.height = height
        self.side1=side1
        self.side2=side2
        self.side3=side3
    def calculate_area(self):
        return 0.50*self.base*self.height
    def calculate_perimeter(self):
        return self.side1+self.side2+self.side3
r=7
circle=circle(r)
circle_area=circle.calculate_area()
circle_perimeter=circle.calculate_perimeter()
w=7
l=5
rectangle=rectangle(l,w)
rectangle_area=rectangle.calculate_area()
rectangle_perimeter=rectangle.calculate_perimeter()
base=5
height=4
s1=4
s2=3
s3=5
triangle=triangle(base,height,s1,s2,s3)
triangle_area=triangle.calculate_area()
triangle_perimeter=triangle.calculate_perimeter()
print("radius of circle: ",r)
print("Area of a circle: ", circle_area)
print("Perimeter of a circle: ", circle_perimeter)
print("lenght and width of a rectangle: ",w,l)
print("Area of a rectangle is: ",rectangle_area)
print("perimeter of a rectangle is: ", rectangle_perimeter)
print("height,base,side1,side2,side3 is: ",base,height,s1,s2,s3)
print("Area of a triangle is : ",triangle_area )
print("perimeter of a triangle is: ",triangle_perimeter)



        
    
    