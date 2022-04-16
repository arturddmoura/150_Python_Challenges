# After gathering the four names, ages and shoe sizes, ask the user to enter the name of the person they want to remove from the list. 
# Delete this row from the data and display the other rows on separate lines.
list = {}

for i in range (0,3):
    name = input("Name: ")
    age = int(input("Age: "))
    size = int(input("Shoe size: "))
    list[name] = {"Age": age, "Size": size}

delete = input("Who do you want to delete from the list? ")
del list[delete]

for name in list:
    print((name), list[name]["Age"], list[name]["Size"])