file_name = "list.txt"
mode = "r" # r = read data from file
file = open(file_name,mode) #open file list.txt in read mode and store reference of it in variable file

#read data from line by line & display 
for line in file: 
    print(line.strip())
file.close() # close file
