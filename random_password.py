# this example explain how we can use string and ramdom module to randomly generate password 
'''
    we need string which has all letter in lower & uppercase & digits and symbols as well
    then we need to findout length of such string 
    we need to pick N number of random letters from that string, we will store into another list
    then we will join all the letters and return it as string
'''
import random as rd 
import string as st 
def GeneratePassword(length=10):
    line = st.ascii_lowercase + st.ascii_uppercase + st.digits  + '!@#$%^&*()-=[]{}<>?.,'
    size = len(line) 
    # print(line,size)
    password = [] #empty list
    count = 0
    while count<length:
        any_letter = line[rd.randint(0,size-1)]
        password.append(any_letter)
        count=count+1
    return "".join(password)

print(GeneratePassword())
print(GeneratePassword(length=20))
print(GeneratePassword(length=30))