#create function that generate otp(one time password) of 6 digit
import random as rd 
def getOTP():
    num1 = rd.randint(10,99) # 45
    num2 = rd.randint(10,99) # 73
    num3 = rd.randint(10,99) # 11
    otp = str(num1) + str(num2) + str(num3)
    return otp

otp = getOTP()
print(otp)
