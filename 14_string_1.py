# example of string related libarary function 
name = input("Enter your full name")
print(name)
print(name.lower()) 
print(name.upper())
print(len(name))
print("is this string has only alphabets and numbers",name.isalnum())
print("is this string has only alphabets ",name.isalpha())
print("is this string has only numbers",name.isdigit())

print("is this string is in lowercase",name.islower())
print("is this string is in uppercase",name.isupper())
print("is this string is in title case",name.istitle())

print("has this string only has space",name.isspace())