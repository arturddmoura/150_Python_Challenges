#  Using the Books.csv file, ask the user how many records they want to add to the list and then allow them to add that many.
#  After all the data has been added, ask for an author and display all the books in the list by that author. 
#  If there are no books by that author in the list, display a suitable message

add_records = int(input("How many records do you want to add? "))

for i in range(0, add_records):
    file = open("Books.csv", "a")

    title = input("Please enter a book title: ")
    author = input("Please enter the author: ")
    year = input("Please enter the year: ")

    newbook = title + ", " + author + ", " + year + "\n"
    file.write(str(newbook))
    file.close()

search = input("Please enter an author: ")

file = open("Books.csv", "r")
count = 0
for row in file:
    if search in str(row):
        print(row)
        count = count + 1
file.close()
        
if count == 0:
    print(f"There are no books by {search}.")
