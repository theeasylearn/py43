# example of using math module
import math 
number = float(input("Eneter float number")) #5.23
print(number) 
result = math.ceil(number)  # 6
print(result)

result2 = math.floor(number) # 5
print(result2)

#better choice is trunc function to round value in case of negative values
result3 = math.trunc(number) # 5
print(result3)

number2 = int(input("Enter number to get it's factorial"))
result4 = math.factorial(number2)
print(result4)

number3 = int(input("Enter one integer negative number"))
result5 = math.fabs(number3)
print(result5)

result6 = math.fmod(10,3) # 10%3
print("result of 10%3 =",result6)

result7 = math.copysign(result5,-1) 
print(f"{result5} variable value as negative value = ",result7)


