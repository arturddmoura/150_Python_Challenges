#If the user selects 1, allow them to add to a file called Salaries.csv which will store their name and salary. 
# If they select 2 it should display all records in the Salaries.csv file. If they select 3 it should stop the program. 
# If they select an incorrect option they should see an error message. They should keep returning to the menu until they select option 3.
import csv

def addSalaries():
    file = open("Salaries.csv", "a")

    name = input("Please enter your name: ")
    salary = input("Please enter your salary: ")

    add = name + ', ' + salary + '\n'
    file.write(str(add))
    file.close()

def displaySalaries():
    file = open ("Salaries.csv", "r")
    for row in file:
        print(row)
    file.close()

def main():
    running = True
    while running == True:
        option = int(input("1) Add to file.\n2) View all records.\n3) Quit program.\nPlease select an option: "))

        if option == 1:
            addSalaries()
        
        elif option == 2:
            displaySalaries()
        
        elif option == 3:
            running = False
        
        else:
            print("Invalid option!")

main()