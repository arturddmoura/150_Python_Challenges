# Ask the user to enter the name, age and shoe size for four people. 
# Ask for the name of one of the people in the list and display their age and shoe size.

list = {}

for i in range (0,4):
    name = input("Name: ")
    age = int(input("Age: "))
    size = int(input("Shoe size: "))
    list[name] = {"Age": age, "Size": size}

user = input("Whose shoe size and age do you want to know? ")
print(list[user])