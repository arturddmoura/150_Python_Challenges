#Import the data from the Books.csv file into a list. Display the list to the user. Ask them to select which row from the list they want to delete and remove it from the list. Ask the user which data they want to change and allow them to change it. Write the data back to the original .csv file, overwriting the existing data with the amended data
import csv

x = 0
y = 0

#display csv to user
file = open("Books.csv", "r")
for row in file:
    print(f"{x} - {row}")
    x = x + 1
file.close()

#open csv as list
file = list(csv.reader(open("Books.csv")))
temp = []

for row in file:
    temp.append(row)

#delete row from csv
delete = int(input("Which row do you want to delete? "))
del temp[delete]

#value change
row_change = int(input("Which row do you want to change? "))
value_change = int(input("Which value? "))
text = input("What do you want to change it to? ")
temp[row_change][value_change] = text

#write to original csv file
file = open("Books.csv", "w")

for row in temp:
    new_line = temp[y][0] + ", " + temp[y][1] + ", " + temp[y][2] + "\n"
    file.write(new_line)
    y = y + 1

file.close()