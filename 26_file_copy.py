import shutil 
filename = input("Enter file to copy")
copy_filename = input("Enter new file name to copy file")
shutil.copy(filename,copy_filename)
print("file has been copied successfully")