#concept of hiearchical inheritance 
#MyMath is the parent class
class MyMath:
    def getPi(self):
        pi = 3.1415
        return pi 
    def getSquare(self,number):
        square = number * number
        return square

#child class 
class Circle(MyMath):
    def __init__(self,radius):
        super().__init__() #calling parent class 
        #instance variable
        self.radius = radius
    def getArea(self):
        #calculate and return area 
        #local variable
        area = super().getPi() * super().getSquare(self.radius)
        return area
    
#child class 
class Square(MyMath):
    def __init__(self,size):
        super().__init__() #parent class construcot is called
        #instance variable
        self.size = size
    def getArea(self):
        area = super().getSquare(self.size)
        return area 
    

radius = int(input("Enter radius"))
#create object Circle class 
c1 = Circle(radius) #call constructor 
area = c1.getArea()
print(f" circle area = {area}")

#create object Square class
size = int(input("Enter size"))
s1 = Square(size)

area2 = s1.getArea()
print(f" square area = {area2}")


