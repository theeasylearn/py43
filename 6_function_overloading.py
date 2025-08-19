#example of function/method overloading 
class Area:
    # here we have used default argument function to implement concept of method overloading
    def compute(self,length=0,width=0):
        if length !=0 and width !=0:
            return length * width
        elif length!=0: 
            return length * length
        else: 
            return 0

a1 = Area()
length = int(input("Enter length"))
width = int(input("Enter width"))
result = a1.compute(length,width)
print(f"area = {result}")

result = a1.compute(length)
print(f"area = {result}")

result = a1.compute()
print(f"area = {result}")

