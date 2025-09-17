#pick one or more item from list
import random
cakes = [
    "Chocolate Cake","Vanilla Cake","Red Velvet Cake","Black Forest Cake","Cheesecake","Carrot Cake","Pineapple Cake","Strawberry Cake","Coffee Cake","Marble Cake","Fruit Cake","Banana Cake","Butter Cake","Sponge Cake","Lemon Cake","Chiffon Cake","Tiramisu Cake","Opera Cake","Cupcakes","Ice Cream Cake"
]
# print(cakes) 

#pick any one cake
# print (random.choice(cakes)) 

#pick any 2 cate
# print(random.choices(cakes,k=2))

countries = ["Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kazakhstan", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom", "Vatican City"]

print("before shuffling")
print(countries)
random.shuffle(countries)
print("after shuffling")
print(countries)
print(random.sample(countries,5))
