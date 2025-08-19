#concept of private variable
class Account:
    #constructor
    def __init__(self,name,type,balanace):
        #public instance variable (properties)
        self.name = name 
        self.type = type
        #private instance variable
        self.__balance = balanace
    def updateBalance(self,amount):
        self.__balance = amount 
    def display(self):
        print(f"name = {self.name} acc type = {self.type} balance = {self.__balance}")

#create object 
a1 = Account("Ankit Patel",'Current Account',2500000)
a1.updateBalance(100) #it will increase my balance by 100 Rs 
a1.display()
a1.updateBalance(-99)
a1.display()
a1.name = "Jiya Patel" # will update name 
a1.balance = 10000000 #will be ignored
a1.display()
# print(a1.__balance) #we can not access private variable using object outside class 