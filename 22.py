#Ask the user to enter their first name and surname in lower case. Change the case to title case and join them together. Display the finished result.

name = input("Enter your name in lower case: ")
surname = input("Enter your surname in lower case: ")

name = name.title() + " " + surname.title()
print(name)