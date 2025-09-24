# example of join and split 
countries = ["Canada", "Brazil", "India", "Kenya", "France", "Japan", "Australia", "Mexico", "Italy", "South Korea", "South Africa", "Germany", "Argentina", "Thailand", "Spain", "Norway", "Turkey", "Vietnam", "United Kingdom", "Egypt"]
print(countries)
# #now i want to convert this list into string 
connector = " " #space as separator between two words 
print(connector.join(countries)) #it will return & display string which has all the countries name 
letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9"
print(letters)
print(letters.split())
line = "India is a land of diversity, India has a rich history, India celebrates many festivals, India is known for its unity, and India inspires the world."
print(line)
print(line.replace("India","Bharat")) # it will replace each and every india 
print(line.replace("India","Bharat",1)) #it will replace only 1st india
