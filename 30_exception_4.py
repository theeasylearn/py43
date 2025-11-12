# example of how to raise custom exception
#write a program to accept age from user and then check age, if age is under 18 raise an exception you can not buy action movie ticket else allow him to buy ticket
try:
    age = int(input("Enter your age"))
    if age<18:
        raise ValueError("you can not buy action movie because of your age is below 18. sorry")
    else:
        print("Enjoy movie, please come again")
except ValueError as error:
    print(f"hey we got run time error and it is {error}")
finally:
    print("Thank you for visiting us")