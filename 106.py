#Create a new file called “Names.txt”. 
# Add five names to the document, which are stored on separate lines. 
# Once you have run the program, look in the location where your program is stored
#  and check that the file has been created properly.
file = open("Names.txt", "w")

file.write("Artur\n")
file.write("Vitor\n")
file.write("Raquel\n")
file.write("Adriane\n")
file.write("Paulo\n")

file.close