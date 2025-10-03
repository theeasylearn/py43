#how to rename file
import os 
file_name = input("Enter file existing file name to rename")
new_file_name = input("Enter new file name ")
try:
    os.rename(file_name,new_file_name)
    print("File renamed successfully")
except FileNotFoundError:
    print("no such file exist",file_name)
except FileExistsError:
    print("file already exist",new_file_name)