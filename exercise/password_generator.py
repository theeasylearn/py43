# Password Generator
# Create a program that generates a random 6-character that has letters and digits.
import string as st 
import random as rd 
def GeneratePassword():
    letters = st.ascii_lowercase + st.digits
    size = len(letters) - 1
    print(letters)
    # print(position)
    password = ''
    for count in range(0,6): # 0 1 2 3 4 5 
         position = rd.randint(0,size)
         password = password + letters[position]
    return password


#call function
password = GeneratePassword()
print(password)