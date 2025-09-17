import random as rd #rd is alias name (nick name) 
number = rd.random() #it will return float random number between 0.0 and 1.0 
print(number)

#another integer random number between 10 and 99
number2 = rd.randint(10,99) 
print(number2)
#another float randome number between 100,1000
number3 = rd.uniform(100,1000)
print(number3)

#another integer random number using rangerange
number4 = rd.randrange(10,100,5)
print(number4)
