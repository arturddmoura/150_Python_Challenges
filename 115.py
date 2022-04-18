#Using the Books.csv file, display the data in the file along with the row number of each.
import csv

file = open("Books.csv", "r")
x = 0

for row in file:
    print(f"Row {x}: {row}")
    x = x + 1