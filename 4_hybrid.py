#this is an example of hybrid inheritance 
# MyMath is inherited in Square class so it is single level inheritance
# Square is inherited in Garden class so it is multi level inheritance
# Square & LandScape is inherited in Garden class so it is multiple inheritance 
# because of all above inheritance, this example is of hybrid inheritance

class MyMath:
    def getSquare(self,number):
        result = number * number
        return result
    
class Square(MyMath):
    def __init__(self,size):
        self.size = size 
    def getArea(self):
        area = super().getSquare(self.size)
        return area 

class Landscape:
    def __init__(self,length,width):
        self.length = length
        self.width = width 
    def getArea(self):
        area = self.length * self.width
        return area 

#multilevel inheritance
class Garden(Square,Landscape):
    def __init__(self, size,length,width):
        #required
        Square.__init__(self,size) 
        Landscape.__init__(self,length,width)
    #method Overidding
    def getArea(self):
        area = Square.getArea(self)
        area2 = Landscape.getArea(self)
        totalarea = area + area2
        return totalarea
    
size = int(input("Enter Square size"))
length = int(input("Enter Landscape length"))
width = int(input("Enter Landscape width"))
g1 = Garden(size,length,width)
totalarea = g1.getArea()
print(f"Garden total area = {totalarea}")