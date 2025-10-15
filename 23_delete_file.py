#example of delete file 
import os 
filename = input("Enter file name")
try:
    os.remove(filename)
except FileNotFoundError:
    #except block will execute only if file does not exists
    print("file does not exists")
except PermissionError:
    #except block will execute only if name is directory not a file
    print("it is directory/folder. it is not file")
else:    
    #else block will execute if file has been deleted successfully
    print("File has been deleted")
