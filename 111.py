#Create a .csv file that will store the following data. Call it “Books.csv”.

import csv

file = open("Books.csv", "w")
book = ("To Kill a Mocking Bird, Harper Lee, 1960\n")
file.write(str(book))
book = ("A Brief History of Time, Stephen Hawking, 1988\n")
file.write(str(book))
book = ("The Great Gatsby, F. Scott Fitzgerald, 1922\n")
file.write(str(book))
book = ("The Man Who Mistook his Wife for a Hat, Oliver Sacks, 1985\n")
file.write(str(book))
book = ("Pride and Prejudice, Jane Austeen, 1813\n")
file.write(str(book))
file.close()