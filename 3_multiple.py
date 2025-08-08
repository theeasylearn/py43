#this is an example of multiple inheritance 
class Square:
    def __init__(self,size):
        self.size = size 
    def getArea(self):
        area = self.size * self.size 
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