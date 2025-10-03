file_name = "friends.txt"
mode = "w"
#open file in write mode (if file does not exist, new file will be created, else existing file data will be replaced(overwrite) by new data)
with open(file_name,mode) as file:
    while True:
        name = input("Enter your friend name type exit to end program")
        if name == 'exit' or name == 'EXIT':
            break # will break(stop) loop 
        else:
            file.write(name + "\n")
    print("data has been write to file successfully.")
