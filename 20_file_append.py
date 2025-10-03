file_name = "friends.txt"
mode = "a" # this will add new data at the end of file
#open file in append mode means if file does not exist, new file will be created, else existing file data will be appended add at the end of existing file)
with open(file_name,mode) as file:
    while True:
        name = input("Enter your friend name type exit to end program")
        if name == 'exit' or name == 'EXIT':
            break # will break(stop) loop 
        else:
            file.write(name + "\n")
    print("data has been write to file successfully.")
