#Ask the user to enter their first name and then ask them to enter their surname. Join them together with a space between and display the name and the length of whole name.

name = input("Enter your name: ")
surname = input("Enter your surname: ")

n1 = len(name)
n2 = len(surname) + n1

name = name + " " + surname

print(name)
print(f"Your name is {n2} letters long.")