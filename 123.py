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

def deleteSalaries():
    file = list(csv.reader(open("Salaries.csv")))

    temp = []

    for row in file:
        temp.append(row)

    num = 0
    for row in temp:
        print(f"{num} - {row}")
        num = num + 1

    delete = int(input("Which row do you want to delete? "))
    del temp[delete]

    file = open("Salaries.csv", "w")

    y = 0
    for row in temp:
        new_line = temp[y][0] + ", " + temp[y][1] + "\n"
        file.write(new_line)
        y = y + 1

    file.close()


def main():
    running = True
    while running == True:
        option = int(input("1) Add to file.\n2) View all records.\n3) Delete a record.\n4) Quit program.\nPlease select an option: "))

        if option == 1:
            addSalaries()
        
        elif option == 2:
            displaySalaries()

        elif option == 3:
            deleteSalaries()
        
        elif option == 4:
            running = False
        
        else:
            print("Invalid option!")

main()