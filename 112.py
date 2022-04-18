#Using the Books.csv file from program 111, ask the user to enter another record and add it to the end of the file. Display each row of the .csv file on a separate line.
import csv

file = open("Books.csv", "a")
title = input("Please enter a book title: ")
author = input("Please enter the author: ")
year = input("Please enter the year: ")
newbook = title + ", " + author + ", " + year + "\n"
file.write(str(newbook))
file.close()

file = open("Books.csv", "r")
for row in file:
    print(row)
file.close()