file_name = "list.txt"
mode = "r" # r = read data from file
file = open(file_name,mode) #open file list.txt in read mode and store reference of it in variable file

#read whole file using single read function
content = file.read()
print(content) #display content variable which has file's content
file.close()