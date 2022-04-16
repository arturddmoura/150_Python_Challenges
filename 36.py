#Alter program 035 so that it will ask the user to enter their name and a number and then display their name that number of times.
name = input("Please enter your name: ")
loop = int(input("Please enter a number: "))
count = 0

while count < loop:
    print(name)
    count = count + 1