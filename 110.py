#Using the Names.txt file you created earlier, display the list of names in Python. 
#Ask the user to type in one of the names and then save all the names 
# except the one they entered into a new file called Names2.txt.
file = open("Names.txt", "r")
print(file.read())
file.close()

file = open("Names.txt", "r")
delete = input("Which of the names do you wish to delete? ")
delete = delete + "\n"

for row in file:
    if row != delete:
        new_file = open("Names2.txt", "a")
        new_row = row
        new_file.write(new_row)
        new_file.close()

file.close()
