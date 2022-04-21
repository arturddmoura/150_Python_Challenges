#Create a program that will allow the user to easily manage a list of names. 
# You should display a menu that will allow them to add a name to the list, change a name in the list, delete a name from the list or view all the names in the list. 
# There should also be a menu option to allow the user to end the program. 
# If they select an option that is not relevant, then it should display a suitable message. 
# After they have made a selection to either add a name, change a name, delete a name or view all the names, they should see the menu again without having to restart the program. 
# The program should be made as easy to use as possible.
list = []

def addName():
    name_add = input("Insert the name you want to add: ")
    list.append(name_add)

def deleteName():
    name_del = input("Inser the name you want to delete: ")
    list.remove(name_del)

def viewNames():
    x = 1
    for i in list:
        print(f"{x} - {i}")
        x = x + 1

def changeName():
    x = 1
    for i in list:
        print(f"{x} - {i}")
        x = x + 1

    name_choice = int(input("Please enter the name you want to change: "))
    new_name = input("Please enter the name you want to change it to: ")
    list[name_choice - 1] = new_name

def main():
    running = True
    while running == True:
        user_option = int(input("1) Add a name.\n2) Delete a name.\n3) Change a name.\n4) Display list.\n5) Stop program.\nSelect an option: "))

        if user_option == 1:
            addName()
        
        elif user_option == 2:
            deleteName()
        
        elif user_option == 3:
            changeName()

        elif user_option == 4:
            viewNames()

        elif user_option == 5:
            running = False
    
main()