import os 
filename = input("Enter file name to check exists or not")
if os.path.exists(filename):
    print("file does exists")
else:
    print("file does not exists at all")
print("Good bye.")