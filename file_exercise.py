file_name = "festivals.txt"
mode = "w" 
#open file in write mode (if file does not exist, new file will be created, else existing file data will be replaced(overwrite) by new data)
with open(file_name,mode) as file:
    count = 1
    while count<=10:
        name = input("Enter festival name ")
        file.write(name + "\n")
        count = count + 1
    print("data has been write to file successfully.")
