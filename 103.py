#Adapt program 102 to display the names and ages of all the people in the list but do not show their shoe size.
list = {}

for i in range (0,4):
    name = input("Name: ")
    age = int(input("Age: "))
    size = int(input("Shoe size: "))
    list[name] = {"Age": age, "Size": size}

for name in list:
    print((name), list[name]["Age"])