# concept of global variable
amount = 2000
def addMoney(value):
    # global amount # means in this method it will access global variable amount
    amount = 0 # it is local variable
    amount = amount + value 

print(amount) # 2000
value = int(input("Enter amount you want to add in your bank account")) # 100
addMoney(value) 
print(amount) # 300

