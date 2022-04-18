#Using the Books.csv file, ask the user to enter a starting year and an end year. Display all books released between those two years.
import csv

file = list(csv.reader(open("Books.csv")))
temp = []

user_start = int(input("Please enter a starting year: "))
user_end = int(input("Please enter an end year: "))

for row in file:
    temp.append(row)

x = 0
for row in temp:
    if int(temp[x][2]) >= user_start and int(temp[x][2]) <= user_end:
        print(temp[x])
    x = x + 1
