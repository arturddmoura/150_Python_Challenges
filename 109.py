#Display the following menu to the user:
menu = int(input("1) Create a new file.\n2) Display new file.\n3) Add a new item to the file.\nSelect 1, 2 or 3: "))

#Ask the user to enter 1, 2 or 3. If they select anything other than 1, 2 or 3 it should display a suitable error message.
while menu != 1 and menu != 2 and menu != 3:
    print("Invalid option, please try again! ")
    menu = int(input("1) Create a new file.\n2) Display new file.\n3) Add a new item to the file.\nSelect 1, 2 or 3: "))

# If they select 1, ask the user to enter a school subject and save it to a new file called “Subject.txt”. 
#  It should overwrite any existing file with a new file.
if menu == 1:
    file = open("Subject.txt", "w")
    file.close()

#If they select 2, display the contents of the “Subject.txt” file.
if menu == 2:
    file = open("Subject.txt", "r")
    print(file.read())
    file.close()

# If they select 3, ask the user to enter a new subject 
# and save it to the file and then display the entire contents of the file.
if menu == 3:
    file = open("Subject.txt", "a")
    user = input("Please enter a new subject: ")
    file.write(user + "\n")
    file.close()

    file = open("Subject.txt", "r")
    print(file.read())
    file.close()