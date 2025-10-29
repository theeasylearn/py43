# Count Vowels
# Ask the user to enter a word and count how many vowels (a, e, i, o, u) are in it.
line = input("Enter one line of text(like name or address)")
#line = ankit (5)
# output = vowels = 2
vowels = 0
size = len(line)
for count in range(0,size):
    if line[count] == 'a' or line[count] == 'e' or line[count] == 'i' or line[count] == 'o' or line[count] == 'u':
        vowels= vowels+1
    
print("vowels = ",vowels)
