#Change program 037 to also ask for a number. Display their name (one letter at a time on each line) and repeat this for the number of times they entered.

name = input("Please enter your name: ")
number = int(input("Please enter a number: "))

for x in range (0, number):
    for i in name:
        print(i)