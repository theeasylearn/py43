#how to work with file management along with exception handling mechanism 
#exception (run time error)
file_name = "friends.txt"
mode = "r"
try:
    with open(file_name,mode) as file:
        content = file.read() # will read whole file 
        print(content)
        print("program finished successfully")
except FileNotFoundError:
    print("file does not exists. ",file_name)
except PermissionError:
    print("you do not have persmission to read file")