# how to create, delete, change & get directory
import os 
foldername = input("Enter folder name you want to create")
os.mkdir(foldername)
print("folder has been create")

foldername = input("Enter folder name you want to delete")
os.rmdir(foldername)
print("folder has been deleted")

print("current directory name ",os.getcwd()) #it will return current directory name

os.chdir('family') #it will change current working directory 
print("current directory name ",os.getcwd()) #it will return current directory name
